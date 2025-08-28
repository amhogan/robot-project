#!/usr/bin/env python3
import time, sys
from roboclaw_3 import Roboclaw   # will use roboclaw_3.py we drop in same folder

PORTS = ["/dev/ttyACM0", "/dev/ttyUSB0"]
BAUD  = 38400
ADDR  = 0x80  # 128

def open_rc():
    last = None
    for p in PORTS:
        try:
            rc = Roboclaw(p, BAUD)
            rc.Open()
            return rc, p
        except Exception as e: last = e
    print("Could not open ports", PORTS, "\nLast error:", last); sys.exit(1)

def stop(rc):
    try:
        rc.ForwardM1(ADDR,0)
        rc.ForwardM2(ADDR,0)
    except Exception: pass

def status(rc):
    try:
        ok1, main = rc.ReadMainBatteryVoltage(ADDR)
        ok2, logic = rc.ReadLogicBatteryVoltage(ADDR)
        ok3, e1    = rc.ReadEncM1(ADDR)
        ok4, e2    = rc.ReadEncM2(ADDR)
        print(f"Main={main/10:.1f}V Logic={logic/10:.1f}V Enc=({e1},{e2})")
    except Exception as e:
        print("Status read failed:", e)

def pulse(rc, fn, label, power=64, dur=2.0):
    print(label)
    fn(ADDR, power)
    time.sleep(dur)
    stop(rc)
    time.sleep(0.5)
    status(rc)

def main():
    rc, port = open_rc()
    print(f"Connected on {port} @ {BAUD}, addr {ADDR}")
    try:
        ok, ver = rc.ReadVersion(ADDR)
        print("FW:", ver.decode(errors="ignore") if ok else "unknown")
        status(rc)
        print("=== M1 ==="); pulse(rc, rc.ForwardM1, "M1 fwd 50%"); pulse(rc, rc.BackwardM1, "M1 rev 50%")
        print("=== M2 ==="); pulse(rc, rc.ForwardM2, "M2 fwd 50%"); pulse(rc, rc.BackwardM2, "M2 rev 50%")
        print("Done.")
    finally:
        stop(rc)

if __name__ == "__main__":
    main()
