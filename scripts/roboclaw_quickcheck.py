#!/usr/bin/env python3
import time
from _rc_util import open_rc

with open_rc() as (rc, cfg, addr):
    duty = int(cfg.get("nudge_duty", 10))
    pause = float(cfg.get("nudge_time_s", 0.5))

    ok, ver = rc.ReadVersion(addr)
    print("Version:", ver.decode("ascii","ignore") if (ok and hasattr(ver,'decode')) else ver)

    def encs(label):
        ok1,e1,_ = rc.ReadEncM1(addr)
        ok2,e2,_ = rc.ReadEncM2(addr)
        print(f"{label} enc: M1={e1 if ok1 else None}  M2={e2 if ok2 else None}")

    encs("start")
    try:
        rc.ForwardM1(addr, duty); rc.ForwardM2(addr, duty); time.sleep(pause)
        rc.ForwardM1(addr, 0);    rc.ForwardM2(addr, 0);    time.sleep(0.2)
        encs("after FWD")

        rc.BackwardM1(addr, duty); rc.BackwardM2(addr, duty); time.sleep(pause)
        rc.BackwardM1(addr, 0);    rc.BackwardM2(addr, 0);    time.sleep(0.2)
        encs("after REV")
        print("Quickcheck complete. (Wheels lifted!)")
    except Exception as e:
        print("[ERR] Motion command failed:", e)
        print("Hints: ensure Motion Studio is closed; USB cable snug; main battery solid; try re-running once.")
        raise
