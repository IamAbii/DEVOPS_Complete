// Placeholder only — used when running via `npm start` for local development.
// In the Docker image, this exact file is overwritten at container START
// (not build time) by generate-env-config.sh, based on the BACKEND_URL
// environment variable the container was given. Never edit the baked-in
// copy inside the image directly; edit generate-env-config.sh instead.
window.APP_CONFIG = {
  backendUrl: ""
};
