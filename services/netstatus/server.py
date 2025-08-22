from flask import Flask, jsonify
import psutil, time, os

app = Flask(__name__)

@app.get("/status")
def status():
    load1, load5, load15 = os.getloadavg()
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return jsonify({
        "cpu": {
            "percent": psutil.cpu_percent(interval=0.2),
            "load_avg": [load1, load5, load15]
        },
        "mem": {
            "total": mem.total,
            "used": mem.used,
            "percent": mem.percent
        },
        "disk": {
            "total": disk.total,
            "used": disk.used,
            "percent": round(disk.used/disk.total*100, 1)
        }
    })

@app.get("/status_temp")
def status_temp():
    temp_c = None
    try:
        temps = psutil.sensors_temperatures()
        for key in ("cpu-thermal","cpu_thermal","soc_thermal","coretemp"):
            if key in temps and temps[key]:
                temp_c = temps[key][0].current
                break
    except Exception:
        pass
    return jsonify({"cpu_temp_c": float(temp_c) if temp_c is not None else None})

@app.get("/status_uptime")
def status_uptime():
    boot = psutil.boot_time()
    up_s = int(time.time() - boot)
    hrs, rem = divmod(up_s, 3600)
    mins, secs = divmod(rem, 60)
    return jsonify({"uptime_seconds": up_s, "uptime_human": f"{hrs}h {mins}m {secs}s"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
