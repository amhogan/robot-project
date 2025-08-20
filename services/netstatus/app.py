from flask import Flask, jsonify
import psutil, time, os, subprocess

app = Flask(__name__)
BOOT_TIME = psutil.boot_time()

@app.get("/status")
def status():
    d = psutil.disk_usage("/")
    vm = psutil.virtual_memory()
    return jsonify({
        "cpu": {"percent": psutil.cpu_percent(interval=0.2),
                "load_avg": os.getloadavg()},
        "mem": {"total": vm.total, "used": vm.used, "percent": vm.percent},
        "disk": {"total": d.total, "used": d.used, "percent": d.percent},
    })

@app.get("/status_temp")
def status_temp():
    # Prefer Raspberry Pi vcgencmd if present
    try:
        out = subprocess.check_output(["vcgencmd", "measure_temp"], text=True)
        # format: temp=62.0'C
        val = float(out.split("=")[1].split("'")[0])
        return jsonify({"cpu_temp_c": val})
    except Exception:
        temps = psutil.sensors_temperatures()
        for v in temps.values():
            if v:
                return jsonify({"cpu_temp_c": v[0].current})
        return jsonify({"cpu_temp_c": None})

@app.get("/status_uptime")
def status_uptime():
    return jsonify({"uptime_sec": int(time.time() - BOOT_TIME)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
