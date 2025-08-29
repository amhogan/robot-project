#!/usr/bin/env python3
import time
from _rc_util import open_rc

with open_rc() as (rc, cfg, addr):
    duty = int(cfg.get("nudge_duty", 10))
    pause = float(cfg.get("nudge_time_s", 0.5))

    def encs():
        ok1,e1,_ = rc.ReadEncM1(addr)
        ok2,e2,_ = rc.ReadEncM2(addr)
        return (e1 if ok1 else None, e2 if ok2 else None)

    print("Start:", encs())
    print("Forward…")
    rc.ForwardM1(addr, duty); rc.ForwardM2(addr, duty); time.sleep(pause)
    rc.ForwardM1(addr, 0);    rc.ForwardM2(addr, 0);    time.sleep(0.2)
    print("After FWD:", encs())

    print("Reverse…")
    rc.BackwardM1(addr, duty); rc.BackwardM2(addr, duty); time.sleep(pause)
    rc.BackwardM1(addr, 0);    rc.BackwardM2(addr, 0);    time.sleep(0.2)
    print("After REV:", encs())
    print("Done.")
