#!/usr/bin/env python3
# RoboClaw adaptive quick test with explicit "open port" step.

import sys, time

BAUD   = 38400
ADDR   = 0x80
PORTS  = ["/dev/ttyACM0", "/dev/ttyUSB0"]

def import_rc():
    try:
        from tcr_roboclaw import Roboclaw as RC
        return RC, "tcr_roboclaw"
    except Exception:
        pass
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
            raise e
    raise TypeError("No matching constructor for driver")

def ensure_port_open(rc):
    """Try common 'open' methods; ignore if already open."""
    for name in ("Open", "open", "connect", "reopen", "open_port"):
        if hasattr(rc, name):
            try:
                getattr(rc, name)()
                return
            except TypeError:
                # Some variants need (port, baud); try to reuse rc.port/rc.baud/rc.address if present
                port = getattr(rc, "port", None) or getattr(rc, "_port_name", None)
                baud = getattr(rc, "baudrate", None) or getattr(rc, "baud", None)
                if port and baud:
                    try:
                        getattr(rc, name)(port, baud)
                        return
                    except Exception:
                        pass
            except Exception:
                pass
    # Last resort: if driver exposes ._port and ._ser_open() style hooks (rare), we skip poking internals.

def get_method(rc, candidates):
    for n in candidates:
        if hasattr(rc, n):
            return n
    return None

def call(rc, name, *args):
    fn = getattr(rc, name)
    return fn(*args)

def call_addr_or_not(rc, addrless_names, addr_names, *args):
    n = get_method(rc, addrless_names)
    if n:
        return call(rc, n, *args)
    n = get_method(rc, addr_names)
    if n:
        return call(rc, n, ADDR, *args)
    raise AttributeError(f"No method found from {addrless_names} or {addr_names}")

def normalize_tuple(ret):
    if isinstance(ret, tuple) and len(ret) >= 2 and isinstance(ret[0], (bool, int)):
        return ret[1]
    return ret

def status(rc, names):
    try:
        main = call_addr_or_not(rc, names["bat_main_al"], names["bat_main_ad"])
        logic = call_addr_or_not(rc, names["bat_logic_al"], names["bat_logic_ad"])
        e1    = call_addr_or_not(rc, names["enc1_al"], names["enc1_ad"])
        e2    = call_addr_or_not(rc, names["enc2_al"], names["enc2_ad"])
        main  = float(normalize_tuple(main)) / 10.0
        logic = float(normalize_tuple(logic)) / 10.0
        e1    = normalize_tuple(e1)
        e2    = normalize_tuple(e2)
        print(f"Main={main:.1f}V Logic={logic:.1f}V Enc=({e1},{e2})")
    except Exception as e:
        print("Status read failed:", e)

def stop(rc, names):
    for n in (get_method(rc, names["fwd_m1"]), get_method(rc, names["fwd_m2"])):
        if n:
            try:
                call(rc, n, 0)
            except Exception:
                pass

def pulse(rc, names, fwd_key, rev_key, label, power=64, dur=2.0):
    print(label)
    fwd = get_method(rc, names[fwd_key]); rev = get_method(rc, names[rev_key])
    call(rc, fwd, power); time.sleep(dur); stop(rc, names); time.sleep(0.3); status(rc, names)
    call(rc, rev, power); time.sleep(dur); stop(rc, names); time.sleep(0.3); status(rc, names)

if __name__ == "__main__":
    RC, src = import_rc()

    # open the device
    rc = None; used_port_

