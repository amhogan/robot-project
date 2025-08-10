from flask import Flask, jsonify
import time

app = Flask(__name__)

def read_cpu_temp_c():
    path = "/sys/class/thermal/thermal_zone0/temp"
    try:
        with open(path, "r") as f:
            milli_c = int(f.read().strip())
        return milli_c / 1000.0
    except Exception:
        return None

def read_uptime_seconds():
    try:
        with open("/proc/uptime", "r") as f:
            s = float(f.read().split()[0])
        return int(s)
    except Exception:
        return None

@app.route("/status")
def status():
    return jsonify(ok=True, ts=int(time.time()))

@app.route("/status_temp")
def status_temp():
    return jsonify(cpu_temp_c=read_cpu_temp_c())

@app.route("/status_uptime")
def status_uptime():
    return jsonify(uptime_seconds=read_uptime_seconds())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
