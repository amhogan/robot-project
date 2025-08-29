#!/usr/bin/env python3
import time
from _rc_util import open_rc
with open_rc() as (rc, cfg, addr):
    duty = int(cfg.get("nudge_duty", 2)); t=float(cfg.get("nudge_time_s",0.2))
    print("M2 forward tiny…"); rc.ForwardM2(addr, duty); time.sleep(t); rc.ForwardM2(addr, 0); time.sleep(0.2)
    print("M2 reverse tiny…"); rc.BackwardM2(addr, duty); time.sleep(t); rc.BackwardM2(addr, 0); time.sleep(0.2)
    print("Done M2.")
