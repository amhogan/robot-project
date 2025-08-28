#!/usr/bin/env python3
"""
RoboClaw adaptive quick test
- Works with tcr_roboclaw (address bound in ctor, lowercase names) OR BasicMicro style (addressed calls, CamelCase)
- Tries /dev/ttyACM0 then /dev/ttyUSB0
- Spins M1 and M2 forward/back briefly and prints battery+encoders
"""

import sys, time, inspect

BAUD   = 38400
ADDR   = 0x80
PORTS  = ["/dev/ttyACM0", "/dev/ttyUSB0"]

def import_rc():
    # Prefer PyPI package you installed
    try:
        from tcr_roboclaw import Roboclaw as RC
        return RC, "tcr_roboclaw"
    except Exception:
        pass
    # Fallback if you ever drop roboclaw_3.py locally
    try:
        from roboclaw_3 import Roboclaw as RC
        return RC, "roboclaw_3"
    except Exception as e:
        sys.exit(f"Could not import a RoboClaw driver: {e}")

def construct(RC, port):
    # Try (port, baud, addr) then (port, baud)
    for args in [(port, BAUD, ADDR), (port, BAUD)]:
        try:
            return RC(*args)
        except TypeError:
            continue
        except Exception as e:
            # Fail only if the port truly can't be opened
            raise e
    raise TypeError("No matching constructor for driver")

def find_callable(obj, names):
    """Return first attribute that exists on obj from names list, else None."""
    for n in names:
        if hasattr(obj, n):
            return n
    return None

def try_call(rc, name, *args):
    """Call method by name; return (ok, value_or_exc)."""
    try:
        fn = getattr(rc, name)
        return True, fn(*args)
    except Exception as e:
        return False, e

def call_addr_or_not(rc, name_addrless, name_addr, *args):
    """
    Try addrless method first (name_addrless(*args)),
    else addressed method (name_addr(ADDR,*args)).
    """
    if name_addrless and hasattr(rc, name_addrless):
        ok, val = try_call(rc, name_addrless, *args)
        if ok: return val
    if name_addr and hasattr(rc, name_addr):
        ok, val = try_call(rc, name_addr, ADDR, *args)
        if ok: return val
    # If we get here, raise the last error to show what failed
    raise AttributeError(f"Neither {name_addrless} nor {name_addr} worked")

def normalize_tuple(ret):
    """Some APIs return (ok, value) tuples; normalize to value."""
    if isinstance(ret, tuple):
        if len(ret) == 2 and isinstance(ret[0], (bool, int)):
            return ret[1]
    return ret

if __name__ == "__main__":
    RC, src = import_rc()

    # Open serial on first available port
    rc = None
    last = None
    used_port = None
    for p in PORTS:
        try:
            rc = construct(RC, p)
            used_port = p
            break
        except Exception as e:
            last = e
    if rc is None:
        sys.exit(f"Could not open any of {PORTS}. Last error: {last}")

    print(f"Connected via {src} on {used_port} @ {BAUD}, addr {ADDR}")

    # Candidate names for methods across APIs
    names = {
        "ver_addrless": ["read_version", "ReadVersion", "get_version"],
        "ver_addr":     ["ReadVersion"],
        "fwd_m1":       ["forward_m1", "ForwardM1"],
        "rev_m1":       ["backward_m1", "BackwardM1"],
        "fwd_m2":       ["forward_m2", "ForwardM2"],
        "rev_m2":       ["backward_m2", "BackwardM2"],
        "bat_main_al":  ["read_main_battery_voltage", "ReadMainBatteryVoltage"],
        "bat_logic_al": ["read_logic_battery_voltage", "ReadLogicBatteryVoltage"],
        "enc1_al":      ["read_encoder_m1", "ReadEncM1"],
        "enc2_al":      ["read_encoder_m2", "ReadEncM2"],
        # Addressed fallbacks (BasicMicro style)
        "bat_main_ad":  ["ReadMainBatteryVoltage"],
        "bat_logic_ad": ["ReadLogicBatteryVoltage"],
        "enc1_ad":      ["ReadEncM1"],
        "enc2_ad":      ["ReadEncM2"],
    }

    # Resolve which names exist on this driver
    found = {k: find_callable(rc, v) for k, v in names.items()}

    # Firmware
    try:
        ver = call_addr_or_not(rc, found["ver_addrless"], found["ver_addr"])
        ver = normalize_tuple(ver)
        if hasattr(ver, "decode"):
            ver = ver.decode(errors="ignore")
        print("FW:", ver)
    except Exception as e:
        print("ReadVersion failed:", e)

    def status():
        try:
            main = call_addr_or_not(rc, found["bat_main_al"], found["bat_main_ad"])
            logic = call_addr_or_not(rc, found["bat_logic_al"], found["bat_logic_ad"])
            e1 = call_addr_or_not(rc, found["enc1_al"], found["enc1_ad"])
            e2 = call_addr_or_not(rc, found["enc2_al"], found["enc2_ad"])
            main = float(normalize_tuple(main)) / 10.0
            logic = float(normalize_tuple(logic)) / 10.0
            e1 = normalize_tuple(e1)
            e2 = normalize_tuple(e2)
            print(f"Main={main:.1f}V Logic={logic:.1f}V Enc=({e1},{e2})")
        except Exception as e:
            print("Status read failed:", e)

    def stop():
        for n in [found["fwd_m1"], found["fwd_m2"]]:
            if n:
                try: getattr(rc, n)(0)
                except Exception: pass

    def pulse(forward_name, reverse_name, label, power=64, dur=2.0):
        print(label)
        getattr(rc, forward_name)(power)
        time.sleep(dur)
        stop(); time.sleep(0.3); status()
        getattr(rc, reverse_name)(power)
        time.sleep(dur)
        stop(); time.sleep(0.3); status()

    try:
        status()
        # Ensure we found the motion methods
        if not (found["fwd_m1"] and found["rev_m1"] and found["fwd_m2"] and found["rev_m2"]):
            print("Could not resolve motor commands on this driver. Found:", found)
            sys.exit(1)

        print("=== M1 test ===")
        pulse(found["fwd_m1"], found["rev_m1"], "M1 fwd/back 50%")
        print("=== M2 test ===")
        pulse(found["fwd_m2"], found["rev_m2"], "M2 fwd/back 50%")
        print("Done.")
    finally:
        stop()
