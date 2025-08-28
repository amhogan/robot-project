#!/usr/bin/env python3
"""
Final RoboClaw quick test for tcr_roboclaw
- Explicitly opens the serial port (in case the driver didn't)
- Uses address bound in constructor (no address arg per call)
- Spins M1/M2 forward/back briefly and prints status
"""

import time
import sys

PORT = "/dev/ttyACM0"    # change to /dev/ttyUSB0 if needed
BAUD = 38400
ADDR = 0x80              # 128

try:
    from tcr_roboclaw import Roboclaw
except Exception as e:
    print("tcr_roboclaw not installed in this venv:", e)
    sys.exit(1)

# Optional: fall back to pyserial to force-open the port if needed
def ensure_open(rc):
    """
    Many builds open the port in the constructor; some don't.
    If '_port' is None, we use pyserial to open and assign it.
    """
    try:
        # If driver exposes an open/Open/connect method, try that first.
        for name in ("Open", "open", "connect", "reopen", "open_port"):
            if hasattr(rc, name):
                try:
                    getattr(rc, name)()
                    return
                except TypeError:
                    # Try with (port, baud) signature
                    try:
                        getattr(rc, name)(PORT, BAUD)
                        return
                    except Exception:
                        pass
                except Exception:
                    pass
        # If still not open, patch using pyserial
        if getattr(rc, "_port", None) is None:
            import serial
            rc._port = serial.Serial(PORT, BAUD, timeout=0.1)
    except Exception as e:
        print("Failed to open serial port:", e)
        sys.exit(1)

def status(rc):
    try:
        # These methods in tcr_roboclaw do NOT take address args; address is bound in ctor
        main_mv = rc.ReadMainBatteryVoltage()  # may return (ok, mv) or just mv
        logic_mv = rc.ReadLogicBatteryVoltage()
        enc1 = rc.ReadEncM1()
        enc2 = rc.ReadEncM2()

        # normalize tuples like (True, value)
        def val(x):
            if isinstance(x, tuple) and len(x) >= 2 and isinstance(x[0], (bool, int)):
                return x[1]
            return x

        main_v = float(val(main_mv)) / 10.0
        logic_v = float(val(logic_mv)) / 10.0
        e1 = val(enc1)
        e2 = val(enc2)
        print(f"Main={main_v:.1f}V Logic={logic_v:.1f}V Enc=({e1},{e2})")
    except Exception as e:
        print("Status read failed:", e)

def stop(rc):
    try:
        rc.ForwardM1(0)
        rc.ForwardM2(0)
    except Exception:
        pass

def pulse(rc, fwd, rev, label, power=64, dur=2.0):
    print(label)
    fwd(power); time.sleep(dur)
    stop(rc); time.sleep(0.3); status(rc)
    rev(power); time.sleep(dur)
    stop(rc); time.sleep(0.3); status(rc)

if __name__ == "__main__":
    # Construct with address bound (tcr_roboclaw supports this signature)
    rc = Roboclaw(PORT, BAUD, ADDR)

    ensure_open(rc)
    print(f"Connected on {PORT} @ {BAUD}, addr {ADDR}")

    # Firmware (API may be ReadVersion() or read_version(); try both)
    try:
        if hasattr(rc, "ReadVersion"):
            ver = rc.ReadVersion()
        else:
            ver = rc.read_version()
        if isinstance(ver, tuple) and len(ver) >= 2:
            ver = ver[1]
        if hasattr(ver, "decode"):
            ver = ver.decode(errors="ignore")
        print("FW:", ver)
    except Exception as e:
        print("ReadVersion failed:", e)

    try:
        status(rc)
        print("=== M1 ===")
        pulse(rc, rc.ForwardM1, rc.BackwardM1, "M1 fwd/back 50%")
        print("=== M2 ===")
        pulse(rc, rc.ForwardM2, rc.BackwardM2, "M2 fwd/back 50%")
        print("Done.")
    finally:
        stop(rc)
