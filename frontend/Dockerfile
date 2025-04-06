# Stage 1: Build React App
FROM node:18-alpine as build

WORKDIR /app

# Copy package.json only (removed package-lock.json line)
COPY package.json ./

# Install dependencies
RUN npm install

# Copy the full source
COPY . .

# Build the app
RUN npm run build

# Stage 2: Serve the app with NGINX
FROM nginx:alpine

# Copy custom NGINX config if available (optional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Copy built app from previous stage
COPY --from=build /app/build /usr/share/nginx/html

# Add the env.js file for runtime environment injection
COPY public/env.js /usr/share/nginx/html/env.js

# Expose the port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
