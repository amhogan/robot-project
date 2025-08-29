# docker/netstatus/app.py
from __future__ import annotations
import os, json, time, platform
from pathlib import Path
from datetime import datetime, timezone
from flask import Flask, jsonify, make_response
import psutil

app = Flask(__name__)
START_MONO = time.monotonic()

def ok(payload, code=200):
    resp = make_response(jsonify(payload), code)
    resp.headers["Cache-Control"] = "no-store"
    resp.headers["Access-Control-Allow-Origin"] = "*"  # dashboard convenience
    return resp

def get_cpu():
    la1, la5, la15 = psutil.getloadavg() if hasattr(psutil, "getloadavg") else (0,0,0)
    return {
        "percent": psutil.cpu_percent(interval=None),
        "load_avg": [la1, la5, la15],
        "count": psutil.cpu_count(logical=True)
    }

def get_mem():
    vm = psutil.virtual_memory()
    return {"total": vm.total, "used": vm.used, "available": vm.available}

def get_disk():
    du = psutil.disk_usage("/")
    return {"total": du.total, "used": du.used, "free": du.free}

def get_net():
    # Bytes since boot; UI can delta if desired
    io = psutil.net_io_counters()
    return {"bytes_sent": io.bytes_sent, "bytes_recv": io.bytes_recv}

def get_temp():
    # RPi exposes thermal via /sys; psutil may or may not see it
    # Fallback to reading /sys/class/thermal/thermal_zone0/temp if present
    try:
        temps = psutil.sensors_temperatures()
        for name, entries in temps.items():
            for e in entries:
                if e.current is not None:
                    return {"cpu_temp_c": float(e.current)}
    except Exception:
        pass
    p = Path("/sys/class/thermal/thermal_zone0/temp")
    if p.exists():
        try:
            millic = int(p.read_text().strip())
            return {"cpu_temp_c": millic/1000.0}
        except Exception:
            pass
    return {"cpu_temp_c": None}

def get_uptime():
    # monotonic since process start + boot time for absolute
    boot_ts = getattr(psutil, "boot_time", lambda: None)()
    return {
        "uptime_sec": int(time.monotonic() - START_MONO),
        "host_uptime_sec": int(time.time() - boot_ts) if boot_ts else None,
        "now": datetime.now(timezone.utc).isoformat()
    }

def get_battery():
    """
    Pluggable battery source:
      ROBOT_BATT_MODE = mock | file
        mock:   env ROBOT_BATT_V (volts), ROBOT_BATT_I (amps)
        file:   JSON at ROBOT_BATT_SOURCE_FILE {"volts": 24.3, "amps": -0.20}
    Later we’ll add 'roboclaw' mode that reads real-time values.
    """
    mode = os.getenv("ROBOT_BATT_MODE", "mock").lower()
    if mode == "file":
        path = Path(os.getenv("ROBOT_BATT_SOURCE_FILE", "/data/battery.json"))
        if path.exists():
            try:
                data = json.loads(path.read_text())
                v = float(data.get("volts"))
                i = float(data.get("amps"))
                return {"volts": v, "amps": i, "source": "file"}
            except Exception:
                pass
        return {"volts": None, "amps": None, "source": "file", "error": "unreadable"}
    # default mock
    v = float(os.getenv("ROBOT_BATT_V", "24.6"))
    i = float(os.getenv("ROBOT_BATT_I", "-0.21"))
    return {"volts": v, "amps": i, "source": "mock"}

@app.route("/status")
def status():
    return ok({
        "host": platform.node(),
        "cpu": get_cpu(),
        "mem": get_mem(),
        "disk": get_disk(),
        "net": get_net(),
        "temp": get_temp(),
        "uptime": get_uptime()
    })

@app.route("/status_temp")
def status_temp():
    return ok(get_temp())

@app.route("/status_uptime")
def status_uptime():
    return ok({"uptime_sec": get_uptime()["uptime_sec"]})

@app.route("/status_battery")
def status_battery():
    b = get_battery()
    # include simple SOC estimate for 24V lead-acid (very rough, no-load)
    # You can replace this with Roboclaw’s battery min/max later.
    v = b.get("volts")
    soc = None
    if v is not None:
        # naive mapping for 24V LA pack at rest: 25.6V˜100%, 24.0V˜50%, 22.8V˜0%
        soc = max(0.0, min(1.0, (v - 22.8) / (25.6 - 22.8)))
    b["soc_est"] = soc
    return ok(b)

@app.route("/")
def root():
    return ok({"ok": True, "endpoints": ["/status", "/status_temp", "/status_uptime", "/status_battery"]})
