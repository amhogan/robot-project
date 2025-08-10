# Robot Project — State Sheet
_Last updated: 2025-08-10_

## Hardware
- Raspberry Pi 5 (“RPi-Robot”), Ubuntu; USB camera + Wyze (secondary). SSH enabled.
- RoboClaw 2x30 — **stuck in bootloader** (awaiting recovery).
- Future: GPS module (planned).

## Network
- pfSense router; Asus ExpertWiFi EBM68 WAP at 10.22.22.7.
- IPs: eth0 = 10.22.22.34, wlan0 = 10.22.22.35 (prefer eth0 when wired).

## Containers / Services
- ros-core — persistent ✅
- video-dashboard (nginx) — camera + stats ✅
- netstatus (Flask) — CPU/mem ✅; add CPU temp + uptime
- usb-camera — MJPEG/ROS source ✅
- opencv-node — minimal ROS 2 node ✅
- roboclaw-driver — ROS 2 pkg heartbeats; blocked by hardware ⚠️

## Open Issues
1) RoboClaw recovery (reflash)
2) NIC preference (eth0 over wlan0)
3) Add CPU temp + uptime to dashboard
4) FS-i6 → RoboClaw wiring & mapping (post-recovery)
