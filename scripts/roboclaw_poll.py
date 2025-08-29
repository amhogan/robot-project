#!/usr/bin/env python3
import time
from _rc_util import open_rc

with open_rc() as (rc, cfg, addr):
    dt = float(cfg.get("poll_interval_s", 0.3))
    for i in range(10):
        okv, mv = rc.ReadMainBatteryVoltage(addr)
        okc, m1ma, m2ma = rc.ReadCurrents(addr)
        ok1,e1,_ = rc.ReadEncM1(addr)
        ok2,e2,_ = rc.ReadEncM2(addr)
        volts = (mv/10.0) if okv else None
        print(f"{i:02d} V={volts}  I(mA)=({m1ma if okc else None},{m2ma if okc else None})  enc=({e1 if ok1 else None},{e2 if ok2 else None})")
        time.sleep(dt)
