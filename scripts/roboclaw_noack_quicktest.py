#!/usr/bin/env python3
"""
RoboClaw quick test that bypasses ACK on writes.
- Uses tcr_roboclaw
- Skips waiting for ACK so it works on controllers without ACK support
- Spins M1 and M2 forward/back briefly and prints status
"""
import sys, time

PORT = "/dev/ttyACM0"   # change to /dev/ttyUSB0 if needed
BAUD = 38400
ADDR = 0x80             # 128

try:
    from tcr_roboclaw import Roboclaw
except Exception as e:
    print("tcr_roboclaw not installed in this venv:", e)
    sys.exit(1)

def ensure_open(rc):
    """Make sure pyserial port exists and has sensible timeouts."""
    import serial
    if getattr(rc, "_port", None) is None or not getattr(rc._port, "is_open", False):
        rc._port = serial.Serial(PORT, BAUD, timeout=1.5, write_timeout=1.5)
    else:
        rc._port.timeout = 1.5
        rc._port.write_timeout = 1.5

def disable_ack(rc):
    """Patch the driver to not wait for ACK after writes."""
    def _noack(self):
        return True
    rc._writechecksum = _noack.__get__(rc, rc.__class__)

def val(x):
    """Normalize (ok, value) -> value."""
    if isinstance(x, tuple) and len(x) >= 2 and isinstance(x[0], (bool, int)):
        return x[1]
    return x

def status(rc):
    try:
        main = val(rc.ReadMainBatteryVoltage()) / 10.0
        logic = val(rc.ReadLogicBatteryVoltage()) / 10.0
        e1 = val(rc.ReadEncM1())
        e2 = val(rc.ReadEncM2())
        print(f"Main={main:.1f}V Logic={logic:.1f}V Enc=({e1},{e2})")
    except Exception as e:
        print("Status read failed:", e)

def stop(rc):
    try:
        rc.ForwardM1(0)
        rc.ForwardM2(0)
    except Exception:
        pass

def pulse(rc, fwd, rev, label, p=64, dur=2.0):
    print(label)
    fwd(p); time.sleep(dur)
    stop(rc); time.sleep(0.4); status(rc)
    rev(p); time.sleep(dur)
    stop(rc); time.sleep(0.4); status(rc)

if __name__ == "__main__":
    rc = Roboclaw(PORT, BAUD, ADDR)
    ensure_open(rc)
    disable_ack(rc)
    print(f"Connected on {PORT} @ {BAUD}, addr {ADDR}")

    # Firmware is optional; some builds don’t expose the same method
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
        print("=== M1 ==="); pulse(rc, rc.ForwardM1, rc.BackwardM1, "M1 fwd/back 50%")
        print("=== M2 ==="); pulse(rc, rc.ForwardM2, rc.BackwardM2, "M2 fwd/back 50%")
        print("Done.")
    finally:
        stop(rc)
