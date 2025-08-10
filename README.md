# Robot Project

Containers + ROS 2 for a Raspberry Pi 5–based robot with a simple web dashboard.

## Repo layout


## Quick start
```bash
# build + run services
docker build -t netstatus:dev services/netstatus
cd docker
docker compose up -d
# Dashboard → http://<RPi-Robot>:8081/

exit


