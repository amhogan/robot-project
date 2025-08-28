#!/usr/bin/env python3
"""
RoboClaw universal quick test (works with either API style)
- Tries /dev/ttyACM0 then /dev/ttyUSB0
- Baud 38400 (change if your board differs)
- Address 0x80 (128) used when the API requires it
- Spins M1 and M2 forward/back briefly with status reads
"""

import time, sys

BAUD   = 38400
ADDR   = 0x80
PORTS  = ["/dev/ttyACM0", "/dev/ttyUSB0"]

def import_driver():
    # Prefer tcr_roboclaw if installed
    try:
        from tcr_roboclaw import Roboclaw as RC
        return RC, "tcr_roboclaw"
    except Exception:
        pass
    # Fallback to single-file driver in same folder if present
    try:
        from roboclaw_3 import Roboclaw as RC
        return RC, "roboclaw_3"
    except Exception as e:
        print("Could not import RoboClaw driver:", e)
        sys.exit(1)

def construct(RC, port):
    # Try constructor signatures: (port, baud, address) then (port, baud)
    for args in [(port, BAUD, ADDR), (port, BAUD)]:
        try:
            return RC(*args)
        except TypeError:
            continue
        except Exception as e:
            # port open failure -> try next port in caller
            raise e
    raise TypeError("No matching constructor signature for driver.")

def call(rc, name_addrless, name_addr, *args):
    """
    Call rc.<name_addrless>(*args) OR rc.<name_addr>(ADDR, *args),
    whichever exists. Raises last error if neither works.
    """
    last = None
    # addrless: e.g., ReadVersion()
    try:
        fn = getattr(rc, name_addrless)
        return fn(*args)
    except AttributeError as e:
        last = e
    # addr: e.g., ReadVersion(addr)
    try:
        fn = getattr(rc, name_addr)
        return fn(ADDR, *args)
    except AttributeError as e:
        last = e
    raise last

def stop(rc):
    try:
        call(rc, "ForwardM1", "ForwardM1", 0)
        call(rc, "ForwardM2", "ForwardM2", 0)
    except Exception:
        pass

def status(rc):
    try:
        ok1, main = call(rc, "ReadMainBatteryVoltage", "ReadMainBatteryVoltage")
        ok2, logic = call(rc, "ReadLogicBatteryVoltage", "ReadLogicBatteryVoltage")
        ok3, e1    = call(rc, "ReadEncM1", "ReadEncM1")
        ok4, e2    = call(rc, "ReadEncM2", "ReadEncM2")
        # Some drivers don’t return an (ok, value) tuple for voltages/encoders; normalize
        main_v = (main if isinstance(main, (int,float)) else main[0]) if not ok1 else main
        logic_v = (logic if isinstance(logic, (int,float)) else logic[0]) if not ok2 else logic
        e1_v = e1 if isinstance(e1, int) else (e1[0] if isinstance(e1, (tuple,list)) else e1)
        e2_v = e2 if isinstance(e2, int) else (e2[0] if isinstance(e2, (tuple,list)) else e2)
        print(f"Main={float(main_v)/10:.1f}V Logic={float(logic_v)/10:.1f}V Enc=({e1_v},{e2_v})")
    except Exception as e:
        print("Status read failed:", e)

def pulse(rc, forward_name, backward_name, label, power=64, dur=2.0):
    print(label)
    # forward
    call(rc, forward_name, forward_name, power)
    time.sleep(dur)
    stop(rc); time.sleep(0.4); status(rc)
    # backward
    call(rc, backward_name, backward_name, power)
    time.sleep(dur)
    stop(rc); time.sleep(0.4); status(rc)

if __name__ == "__main__":
    RC, src = import_driver()
    # try ports in order
    last_err = None
    rc = None
    used_port = None
    for p in PORTS:
        try:
            rc = construct(RC, p)
            used_port = p
            break
        except Exception as e:
            last_err = e
            rc = None
    if rc is None:
        sys.exit(f"Could not open any of {PORTS}. Last error: {last_err}")

    print(f"Connected via {src} on {used_port} @ {BAUD}, addr {ADDR}")
    try:
        # Firmware
        try:
            ret = call(rc, "ReadVersion", "ReadVersion")
            # Some drivers return (ok, bytes); others return bytes/str
            if isinstance(ret, tuple) and len(ret) >= 2:
                ok, ver = ret[0], ret[1]
                ver = ver.decode(errors="ignore") if hasattr(ver, "decode") else str(ver)
                print("FW:", ver if ok else f"unknown ({ver})")
            else:
                ver = ret.decode(errors="ignore") if hasattr(ret, "decode") else str(ret)
                print("FW:", ver)
        except Exception as e:
            print("ReadVersion failed:", e)

        status(rc)
        print("=== M1 test ===")
        pulse(rc, "ForwardM1", "BackwardM1", "M1 fwd/back 50%")
        print("=== M2 test ===")
        pulse(rc, "ForwardM2", "BackwardM2", "M2 fwd/back 50%")
        print("Done.")
    finally:
        stop(rc)
