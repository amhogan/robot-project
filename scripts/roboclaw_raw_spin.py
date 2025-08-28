#!/usr/bin/env python3
# Raw RoboClaw Packet Serial spin test over USB CDC (no driver dependencies)
# - Control Mode must be Packet Serial; Baud must match; Address must match
# - Sends M1/M2 forward/back using command codes 0,1,4,5 with 7-bit checksum
# - Does not wait for ACK (so it won't block if ACK is disabled/hidden)

import time, serial

PORT = "/dev/ttyACM0"   # change to /dev/ttyUSB0 if needed
BAUD = 19200            # match Motion Studio
ADDR = 0x80             # match Motion Studio

# Packet Serial command codes (BasicMicro)
CMD_M1_FORWARD  = 0    # data: 1 byte (0..127)
CMD_M1_BACKWARD = 1    # data: 1 byte (0..127)
CMD_M2_FORWARD  = 4    # data: 1 byte (0..127)
CMD_M2_BACKWARD = 5    # data: 1 byte (0..127)

def send_pkt(ser, cmd, *data_bytes):
    # 7-bit checksum across address, cmd, and all data bytes
    s = (ADDR + cmd + sum(data_bytes)) & 0x7F
    pkt = bytes([ADDR, cmd, *data_bytes, s])
    ser.write(pkt)
    ser.flush()

def pulse(ser, label, cmd_fwd, cmd_rev, power=127, dur=1.5):
    print(label)
    send_pkt(ser, cmd_fwd, power); time.sleep(dur)
    send_pkt(ser, cmd_fwd, 0);    time.sleep(0.2)
    send_pkt(ser, cmd_rev, power); time.sleep(dur)
    send_pkt(ser, cmd_fwd, 0);    time.sleep(0.2)

if __name__ == "__main__":
    with serial.Serial(PORT, BAUD, timeout=0.2, write_timeout=0.5) as ser:
        print(f"Opened {PORT} @ {BAUD}, addr 0x{ADDR:02X}")
        # Small delay to settle
        time.sleep(0.3)
        # Spin tests (keep wheels off the ground)
        pulse(ser, "M1 fwd/back", CMD_M1_FORWARD, CMD_M1_BACKWARD)
        pulse(ser, "M2 fwd/back", CMD_M2_FORWARD, CMD_M2_BACKWARD)
        print("Done.")
