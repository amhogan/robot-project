#!/usr/bin/env python3
import time, sys
from tcr_roboclaw import Roboclaw

PORT   = "/dev/ttyACM0"         # change to /dev/ttyUSB0 if needed
BAUD   = 19200                   # change to 19200 if you set that in Motion Studio
ADDRS  = [0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87]

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

def read_encs(rc, addr):
    try:
        e1 = val(rc.ReadEncM1(addr))
        e2 = val(rc.ReadEncM2(addr))
        return e1, e2
    except Exception:
        return None, None

def try_addr(addr):
    rc = Roboclaw(PORT, BAUD, addr)
    ensure_open(rc)
    disable_ack(rc)
    print(f"\n=== Trying address 0x{addr:02X} ===")
    # snapshot encoders
    e1a, e2a = read_encs(rc, addr)
    # try Forward/Backward API
    try:
        rc.ForwardM1(addr, 127); time.sleep(1.0); rc.ForwardM1(addr, 0); time.sleep(0.2)
        rc.BackwardM1(addr, 127); time.sleep(1.0); rc.ForwardM1(addr, 0); time.sleep(0.2)
        rc.ForwardM2(addr, 127); time.sleep(1.0); rc.ForwardM2(addr, 0); time.sleep(0.2)
        rc.BackwardM2(addr, 127); time.sleep(1.0); rc.ForwardM2(addr, 0); time.sleep(0.2)
    except TypeError:
        # driver variant without address arg in calls
        rc.ForwardM1(127); time.sleep(1.0); rc.ForwardM1(0); time.sleep(0.2)
        rc.BackwardM1(127); time.sleep(1.0); rc.ForwardM1(0); time.sleep(0.2)
        rc.ForwardM2(127); time.sleep(1.0); rc.ForwardM2(0); time.sleep(0.2)
        rc.BackwardM2(127); time.sleep(1.0); rc.ForwardM2(0); time.sleep(0.2)
    # read encoders again
    e1b, e2b = read_encs(rc, addr)
    moved = (e1a is not None and e1b is not None and (e1b != e1a or e2b != e2a))
    print(f"Encoders before={e1a,e2a} after={e1b,e2b}  moved={moved}")
    return moved

if __name__ == "__main__":
    print(f"Scanning {PORT} @ {BAUD} … (wheels lifted!)")
    any_moved = False
    for a in ADDRS:
        try:
            if try_addr(a):
                print(f"\n✅ Motion detected at address 0x{a:02X}")
                any_moved = True
                break
        except Exception as e:
            print(f"addr 0x{a:02X} error: {e}")
    if not any_moved:
        print("\nNo motion on any common address. Check Packet Serial mode, baud, and E-Stop/brakes.")
