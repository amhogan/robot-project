#!/usr/bin/env python3
"""
RoboClaw diagnostic + spin test (tcr_roboclaw, no-ACK writes)
"""

import sys, time
PORT = "/dev/ttyACM0"
BAUD = 38400
ADDR = 0x80

from tcr_roboclaw import Roboclaw

def ensure_open(rc):
    import serial
    if getattr(rc, "_port", None) is None or not getattr(rc._port, "is_open", False):
        rc._port = serial.Serial(PORT, BAUD, timeout=1.5, write_timeout=1.5)
    else:
        rc._port.timeout = 1.5
        rc._port.write_timeout = 1.5

def disable_ack(rc):
    def _noack(self): return True
    rc._writechecksum = _noack.__get__(rc, rc.__class__)

def val(x):
    if isinstance(x, tuple) and len(x) >= 2 and isinstance(x[0], (bool, int)):
        return x[1]
    return x

def read_error(rc):
    try: return val(rc.ReadError())
    except Exception as ex: return f"err({ex})"

def read_currents(rc):
    try:
        c = rc.ReadCurrents()
        c = val(c)
        if isinstance(c, tuple) and len(c) >= 2:
            return c[0], c[1]
        return c, None
    except Exception:
        return None, None

def status(rc, label=""):
    try:
        main = val(rc.ReadMainBatteryVoltage())/10.0
        logic = val(rc.ReadLogicBatteryVoltage())/10.0
    except Exception:
        main = None; logic = None
    e = read_error(rc)
    i1, i2 = read_currents(rc)
    print(f"{label} Vmain={main}V Vlogic={logic}V Err={e} I(m1,m2)=({i1},{i2})")

def stop(rc):
    try: rc.ForwardM1(0); rc.ForwardM2(0)
    except Exception: pass

def spin_forward_backward(rc, p=127, dur=1.5):
    print("Trying Forward/Backward API")
    status(rc, "before")
    rc.ForwardM1(p); time.sleep(dur); stop(rc); time.sleep(0.3); status(rc, "after M1 fwd")
    rc.BackwardM1(p); time.sleep(dur); stop(rc); time.sleep(0.3); status(rc, "after M1 rev")
    rc.ForwardM2(p); time.sleep(dur); stop(rc); time.sleep(0.3); status(rc, "after M2 fwd")
    rc.BackwardM2(p); time.sleep(dur); stop(rc); time.sleep(0.3); status(rc, "after M2 rev")

def spin_signed_duty(rc, duty=15000, dur=1.5):
    duty_funcs = [("DutyM1","DutyM2"),("DutyM1Signed","DutyM2Signed")]
    for m1name, m2name in duty_funcs:
        if hasattr(rc, m1name) and hasattr(rc, m2name):
            print(f"Trying signed duty via {m1name}/{m2name}")
            m1 = getattr(rc, m1name); m2 = getattr(rc, m2name)
            status(rc, "before")
            m1(+duty); time.sleep(dur); stop(rc); time.sleep(0.3); status(rc, "after M1 +duty")
            m1(-duty); time.sleep(dur); stop(rc); time.sleep(0.3); status(rc, "after M1 -duty")
            m2(+duty); time.sleep(dur); stop(rc); time.sleep(0.3); status(rc, "after M2 +duty")
            m2(-duty); time.sleep(dur); stop(rc); time.sleep(0.3); status(rc, "after M2 -duty")
            return True
    print("No signed duty methods found on this driver")
    return False

if __name__ == "__main__":
    rc = Roboclaw(PORT, BAUD, ADDR)
    ensure_open(rc)
    disable_ack(rc)
    print(f"Connected on {PORT} @ {BAUD}, addr {ADDR}")

    try:
        try:
            ver = rc.ReadVersion() if hasattr(rc, "ReadVersion") else rc.read_version()
            ver = val(ver)
            if hasattr(ver, "decode"): ver = ver.decode(errors="ignore")
            print("FW:", ver)
        except Exception as e:
            print("ReadVersion failed:", e)

        status(rc, "startup")

        # Run both test styles
        spin_forward_backward(rc, p=127, dur=1.5)
        spin_signed_duty(rc, duty=20000, dur=1.5)

        print("Done.")
    finally:
        stop(rc)
