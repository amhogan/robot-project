#!/usr/bin/env python3
import time, serial

PORT = "/dev/roboclaw"
ADDR = 0x80   # 128 decimal

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

def tx(ser, cmd, payload=b""):
    pkt = bytes([ADDR, cmd]) + payload
    crc = crc16_ccitt(pkt)
    ser.write(pkt + bytes([(crc>>8)&0xFF, crc & 0xFF]))
    ser.flush()

with serial.Serial(PORT, 115200, timeout=0.5) as ser:
    ser.reset_input_buffer()
    # Stop both first
    tx(ser, 0, bytes([0]))   # M1 stop
    tx(ser, 4, bytes([0]))   # M2 stop
    time.sleep(0.2)

    print("Twitch M1...")
    tx(ser, 0, bytes([20]))  # Forward M1 speed=20/127
    time.sleep(0.5)
    tx(ser, 0, bytes([0]))   # Stop
    time.sleep(0.2)

    print("Twitch M2...")
    tx(ser, 4, bytes([20]))  # Forward M2 speed=20/127
    time.sleep(0.5)
    tx(ser, 4, bytes([0]))   # Stop

    print("Done.")
