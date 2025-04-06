# Stage 1 - React build
FROM node:18-alpine as builder

WORKDIR /app

# Copy package files and install deps
COPY package*.json ./
RUN npm install

# Copy everything except env.js to prevent build crash
COPY . .

# Delete env.js if exists so React doesn't bundle it
RUN rm -f public/env.js

# Build the React app
RUN npm run build

# Stage 2 - Serve with NGINX
FROM nginx:alpine

# Remove default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy build output from builder
COPY --from=builder /app/build /usr/share/nginx/html

# ✅ Add runtime config after build
COPY public/env.js /usr/share/nginx/html/env.js

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
