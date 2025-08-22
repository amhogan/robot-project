#!/usr/bin/env python3
import time, serial

PORT = "/dev/roboclaw"
ADDR = 0x80  # USB packet-serial address (0x80–0x87 OK)

def crc16_ccitt(data: bytes) -> int:
    crc = 0
    for b in data:
        crc ^= (b << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ 0x1021) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
    return crc

def tx(ser, cmd):
    pkt = bytes([ADDR, cmd])
    c = crc16_ccitt(pkt)
    ser.reset_input_buffer()
    ser.write(pkt + bytes([(c >> 8) & 0xFF, c & 0xFF]))
    ser.flush()

def rx_exact(ser, n, timeout_s=0.5):
    end = time.time() + timeout_s
    buf = bytearray()
    while len(buf) < n and time.time() < end:
        chunk = ser.read(n - len(buf))
        if chunk:
            buf.extend(chunk)
    if len(buf) < n:
        raise RuntimeError(f"Timeout: expected {n} bytes, got {len(buf)}")
    return bytes(buf)

def read_u16(ser, cmd):
    tx(ser, cmd)
    payload = rx_exact(ser, 2)
    rxcrc   = rx_exact(ser, 2)
    calc = crc16_ccitt(bytes([ADDR, cmd]) + payload)
    if rxcrc != bytes([(calc >> 8) & 0xFF, calc & 0xFF]):
        raise RuntimeError(f"CRC mismatch on cmd {cmd}: got {rxcrc.hex()} vs {calc:04x}")
    return (payload[0] << 8) | payload[1]

def read_version_tolerant(ser):
    tx(ser, 21)
    payload = bytearray()
    # read up to 64 bytes until NUL (0x00)
    for _ in range(64):
        b = rx_exact(ser, 1)
        if b == b"\x00":
            nul_seen = True
            break
        payload.extend(b)
    else:
        nul_seen = False
    # read crc
    rxcrc = rx_exact(ser, 2)
    # try CRC over payload (no NUL)
    calc = crc16_ccitt(bytes([ADDR, 21]) + payload)
    if rxcrc == bytes([(calc >> 8) & 0xFF, calc & 0xFF]):
        return bytes(payload).rstrip(b"\n").decode("latin1", "ignore")
    # try CRC over payload+NUL (some fw variants)
    if nul_seen:
        calc2 = crc16_ccitt(bytes([ADDR, 21]) + payload + b"\x00")
        if rxcrc == bytes([(calc2 >> 8) & 0xFF, calc2 & 0xFF]):
            return bytes(payload).rstrip(b"\n").decode("latin1", "ignore")
    # try CRC over payload+"\n"+NUL (rare)
    calc3 = crc16_ccitt(bytes([ADDR, 21]) + payload + b"\n\x00")
    if rxcrc == bytes([(calc3 >> 8) & 0xFF, calc3 & 0xFF]):
        return bytes(payload).rstrip(b"\n").decode("latin1", "ignore")
    # last resort: return the string and warn
    s = bytes(payload).rstrip(b"\n").decode("latin1", "ignore")
    return f"{s} (CRC not matched; tolerated)"

with serial.Serial(PORT, 115200, timeout=0.5) as ser:
    main_0p1V  = read_u16(ser, 24)
    logic_0p1V = read_u16(ser, 25)
    print(f"MainBatt:  {main_0p1V} (0.1V) ~= {main_0p1V/10:.1f} V")
    print(f"LogicBatt: {logic_0p1V} (0.1V) ~= {logic_0p1V/10:.1f} V")
    ver = read_version_tolerant(ser)
    print("Version:", ver)
