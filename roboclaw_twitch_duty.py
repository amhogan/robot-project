#!/usr/bin/env python3
import time, serial

PORT = "/dev/roboclaw"   # use "/dev/ttyACM0" if you didn't make the udev alias
ADDR = 0x80              # 128 decimal

def crc16_ccitt(data: bytes) -> int:
    c=0
    for b in data:
        c ^= (b<<8)
        for _ in range(8):
            c = ((c<<1)^0x1021)&0xFFFF if (c&0x8000) else ((c<<1)&0xFFFF)
    return c

def tx(ser, cmd, payload=b""):
    pkt = bytes([ADDR, cmd]) + payload
    crc = crc16_ccitt(pkt)
    ser.write(pkt + bytes([(crc>>8)&0xFF, crc&0xFF])); ser.flush()

def m1_duty(ser, val):
    if val < 0: val = (1<<16) + val
    tx(ser, 32, bytes([(val>>8)&0xFF, val & 0xFF]))  # cmd 32 = M1 Duty

def m2_duty(ser, val):
    if val < 0: val = (1<<16) + val
    tx(ser, 33, bytes([(val>>8)&0xFF, val & 0xFF]))  # cmd 33 = M2 Duty

with serial.Serial(PORT, 115200, timeout=0.5) as ser:
    ser.reset_input_buffer()
    # Stop both
    m1_duty(ser, 0); m2_duty(ser, 0); time.sleep(0.2)

    twitch = 1500   # ~2.1% duty (gentle)
    print("Duty twitch M1...")
    m1_duty(ser, twitch); time.sleep(0.5); m1_duty(ser, 0); time.sleep(0.2)

    print("Duty twitch M2...")
    m2_duty(ser, twitch); time.sleep(0.5); m2_duty(ser, 0)

    print("Done.")
