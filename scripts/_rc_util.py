import glob, yaml, sys
from pathlib import Path
from contextlib import contextmanager
from roboclaw_3 import Roboclaw

CANDIDATE_PORTS = [f"/dev/ttyACM{i}" for i in range(3)] + [f"/dev/ttyUSB{i}" for i in range(3)]

def load_cfg():
    p = Path(__file__).resolve().parents[1] / "config" / "roboclaw.yaml"
    with open(p, "r") as f:
        return yaml.safe_load(f)

def _try_open(port: str, baud: int, addr: int):
    rc = Roboclaw(port, baud)
    if not rc.Open():
        return None
    ok, _ver = rc.ReadVersion(addr)
    if not ok:
        try: rc.Close()
        except: pass
        return None
    return rc

@contextmanager
def open_rc():
    cfg = load_cfg()
    dev_cfg = cfg["device"]
    baud = int(cfg["baud"])
    addr = int(cfg["address"], 16) if isinstance(cfg["address"], str) else int(cfg["address"])

    ports = []
    if "*" in dev_cfg or "by-id" in dev_cfg:
        ports = glob.glob(dev_cfg)
    if not ports:
        ports = CANDIDATE_PORTS

    rc = None
    for p in ports:
        candidate = _try_open(p, baud, addr)
        if candidate:
            print(f"[rc] Using port: {p} @ {baud} addr=0x{addr:02X}")
            rc = candidate
            break
    if rc is None:
        print(f"[ERR] No RoboClaw detected. Tried: {ports}", file=sys.stderr)
        sys.exit(2)
    try:
        yield rc, cfg, addr
    finally:
        try: rc.Close()
        except: pass
