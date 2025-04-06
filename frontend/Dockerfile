# Stage 1: Build React App
FROM node:18 AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Stage 2: Serve with NGINX
FROM nginx:alpine

# Remove default NGINX config and copy our own
COPY nginx.conf /etc/nginx/nginx.conf

# ✅ Copy built files
COPY --from=build /app/build /usr/share/nginx/html

# ✅ Copy env.js (this must be in public/ before build, or copied after)
COPY public/env.js /usr/share/nginx/html/env.js

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
