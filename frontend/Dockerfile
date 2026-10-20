FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY public/ ./public/
COPY src/ ./src/

RUN npm run build

# Production stage - use nginx
FROM nginx:alpine

# Copy built React app
COPY --from=build /app/build /usr/share/nginx/html

# Configure nginx to serve on port 3000 and handle SPA routing
RUN echo 'server { \
    listen 3000; \
    root /usr/share/nginx/html; \
    location /env-config.js { \
        add_header Cache-Control "no-cache, no-store, must-revalidate"; \
        expires 0; \
    } \
    location / { \
        try_files $uri /index.html; \
    } \
}' > /etc/nginx/conf.d/default.conf

COPY generate-env-config.sh /docker-entrypoint.d/40-generate-env-config.sh
RUN chmod +x /docker-entrypoint.d/40-generate-env-config.sh

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
