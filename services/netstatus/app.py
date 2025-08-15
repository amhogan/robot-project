from flask import Flask, jsonify
import psutil, time, os

app = Flask(__name__)
BOOT_TIME = psutil.boot_time()

def max_temp_c():
    try:
        temps = psutil.sensors_temperatures()
        if not temps:
            return None
        # pick the highest current temp across sensors
        vals = [e.current for arr in temps.values() for e in arr if getattr(e, "current", None) is not None]
        return max(vals) if vals else None
    except Exception:
        return None

@app.get("/healthz")
def healthz():
    return jsonify(status="ok")

@app.get("/metrics.json")
def metrics():
    vm = psutil.virtual_memory()
    du = psutil.disk_usage("/")
    n = psutil.net_io_counters()
    la = os.getloadavg() if hasattr(os, "getloadavg") else (0.0, 0.0, 0.0)
    return jsonify(
        cpu_percent=psutil.cpu_percent(interval=0.1),
        load_avg={"1m": la[0], "5m": la[1], "15m": la[2]},
        mem={"total": vm.total, "used": vm.used, "percent": vm.percent},
        disk={"total": du.total, "used": du.used, "percent": du.percent},
        net_io={"bytes_sent": n.bytes_sent, "bytes_recv": n.bytes_recv},
        temp_c=max_temp_c(),
        uptime_seconds=int(time.time() - BOOT_TIME),
    )

# ---- Legacy endpoints (keep old dashboard/nginx working) ----
@app.get("/status")
def legacy_status():
    """Legacy summary used by the existing dashboard."""
    return jsonify(
        status="ok",
        uptime_seconds=int(time.time() - BOOT_TIME),
        temp_c=max_temp_c()
    )

@app.get("/status_temp")
def legacy_temp():
    """Legacy endpoint: just the temperature (for old widgets)."""
    t = max_temp_c()
    return jsonify(temp_c=t) if t is not None else jsonify(temp_c=None), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
