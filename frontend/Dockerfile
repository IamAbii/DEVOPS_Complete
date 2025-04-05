# ===== Stage 1: Build React App =====
FROM node:20-alpine as builder

# Set working directory
WORKDIR /app

# Copy dependencies
COPY package*.json ./
RUN npm install

# Copy all source files
COPY . .

# Build the React app for production
RUN npm run build

# ===== Stage 2: Serve App with NGINX =====
FROM nginx:stable-alpine

# Remove default NGINX static assets
RUN rm -rf /usr/share/nginx/html/*

# Copy build output from React to NGINX path
COPY --from=builder /app/build /usr/share/nginx/html

# Optional: Copy custom nginx config (if you have one)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]
