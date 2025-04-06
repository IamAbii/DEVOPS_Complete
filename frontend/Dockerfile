# Stage 1: Build React app
FROM node:18-alpine as build

WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm install

COPY . ./
RUN npm run build

# Stage 2: Serve with NGINX
FROM nginx:alpine

# Copy custom NGINX config (optional, see below)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy build output and env.js
COPY --from=build /app/build /usr/share/nginx/html
COPY public/env.js /usr/share/nginx/html/env.js

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
