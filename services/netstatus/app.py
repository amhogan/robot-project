from flask import Flask, jsonify
import psutil, time, os
app = Flask(__name__)
@app.get("/status")
def status():
    la = os.getloadavg() if hasattr(os, "getloadavg") else (0,0,0)
    vm = psutil.virtual_memory(); du = psutil.disk_usage('/')
    return jsonify({
        "cpu":{"percent": psutil.cpu_percent(interval=0.1), "load_avg": la},
        "memory":{"total": vm.total, "used": vm.used},
        "disk":{"total": du.total, "used": du.used},
        "uptime_seconds": time.time() - psutil.boot_time()
    })
@app.get("/status_temp")
def status_temp():
    temp = None
    try:
        temps = psutil.sensors_temperatures()
        for k in temps:
            for t in temps[k]:
                if hasattr(t,'current') and t.current:
                    temp = t.current; break
            if temp: break
    except Exception:
        pass
    return jsonify({"cpu_temp_c": temp})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
