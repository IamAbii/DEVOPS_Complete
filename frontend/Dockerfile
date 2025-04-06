# Stage 1: React build
FROM node:18-alpine as builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# ❌ DO NOT include env.js in src or reference it in build step
RUN npm run build

# Stage 2: Serve using NGINX
FROM nginx:alpine

# Clean default nginx files
RUN rm -rf /usr/share/nginx/html/*

# Copy build
COPY --from=builder /app/build /usr/share/nginx/html

# ✅ Copy env.js into public folder of NGINX
COPY ./frontend/public/env.js /usr/share/nginx/html/env.js

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
