# 0) See what's using space (images/containers/volumes/cache)
docker system df -v
# 1) Remove stopped containers, unused networks, dangling images, build cache
docker system prune -f
# 2) Remove images not used by any container (keeps images backing running containers)
# Keep very recent ones; adjust "until" if you like.
docker image prune -a -f --filter "until=168h"
# 3) Clear builder/cache artifacts (speeds up disk recovery; future builds may take longer)
docker builder prune -af
# 4) OPTIONAL: Remove unused volumes (never removes volumes in use)
# Skip if you're unsure, but generally safe. This does NOT touch bind mounts.
docker volume prune -f
