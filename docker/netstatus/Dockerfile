# docker/netstatus/Dockerfile
FROM python:3.11-slim

# System deps (curl is handy for healthcheck debugging)
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Python deps
RUN pip install --no-cache-dir flask psutil

# App
WORKDIR /app
COPY app.py /app/app.py

# Default envs (override in compose)
ENV TZ=UTC \
    ROBOT_BATT_MODE=mock \
    ROBOT_BATT_V=24.6 \
    ROBOT_BATT_I=-0.21 \
    ROBOT_BATT_SOURCE_FILE=/data/battery.json

EXPOSE 5000
CMD ["python", "/app/app.py"]
