#!/usr/bin/env python3
"""
RoboClaw quick spin test using roboclaw-python
- Tries /dev/ttyACM0 then /dev/ttyUSB0
- 38400 baud (match Motion Studio)
- Spins M1 then M2 forward/back briefly and prints encoder + battery
"""
import time
from roboclaw_python import RoboClaw, Motor

PORTS = ["/dev/ttyACM0", "/dev/ttyUSB0"]
BAUD = 38400
ADDR = 128  # 0x80

def connect():
    last_err = None
    for p in PORTS:
        try:
            rc = RoboClaw(port_name=p, baud_rate=BAUD, address=ADDR, timeout=2, retries=3)
            return rc, p
        except Exception as e:
            last_err = e
    raise RuntimeError(f"Could not open RoboClaw on {PORTS}: {last_err}")

def pulse(rc, motor, value=100, dur=2.0):
    rc.set_speed(motor, value)
    time.sleep(dur)
    rc.set_speed(motor, 0)
    time.sleep(0.5)

def main():
    rc, port = connect()
    print(f"Connected on {port} @ {BAUD} baud addr {ADDR}")

    try:
        # Battery readouts (volts)
        try:
            main_v = rc.read_main_battery() / 10.0
            logic_v = rc.read_logic_battery() / 10.0
            print(f"Battery: Main={main_v:.1f}V Logic={logic_v:.1f}V")
        except Exception as e:
            print("Battery read failed:", e)

        print("=== M1 forward/back ===")
        pulse(rc, Motor.M1, +100, 2.0)
        pulse(rc, Motor.M1, -100, 2.0)

        print("=== M2 forward/back ===")
        pulse(rc, Motor.M2, +100, 2.0)
        pulse(rc, Motor.M2, -100, 2.0)

        # Encoders (optional but nice to confirm motion)
        try:
            e1 = rc.read_encoder(Motor.M1)
            e2 = rc.read_encoder(Motor.M2)
            print(f"Enc(M1,M2)=({e1},{e2})")
        except Exception as e:
            print("Encoder read failed:", e)

        print("Done.")
    finally:
        try:
            rc.set_speed(Motor.M1, 0)
            rc.set_speed(Motor.M2, 0)
        except Exception:
            pass

if __name__ == "__main__":
    main()
