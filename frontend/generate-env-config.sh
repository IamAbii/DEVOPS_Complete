#!/bin/sh
# Runs automatically at CONTAINER START, before nginx starts serving traffic
# (nginx's own official entrypoint executes every script in
# /docker-entrypoint.d/ before it launches nginx — this is not a custom
# hook we invented, it's a feature the base image already provides).
#
# Job: read the BACKEND_URL environment variable this container was given,
# and write it into a small JS file the browser loads before the React
# bundle. This is what makes the image itself environment-agnostic — the
# image never contains a backend address; only a running container does,
# and only because it was told one.
set -eu

: "${BACKEND_URL:=}"

CONFIG_FILE=/usr/share/nginx/html/env-config.js

cat > "$CONFIG_FILE" <<EOF
window.APP_CONFIG = {
  backendUrl: "${BACKEND_URL}"
};
EOF

echo "generate-env-config.sh: wrote BACKEND_URL='${BACKEND_URL}' to ${CONFIG_FILE}"
