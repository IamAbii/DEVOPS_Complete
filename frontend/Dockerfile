# Stage 1 - React build
FROM node:18-alpine as builder

WORKDIR /app

# Install deps
COPY package*.json ./
RUN npm install

# Copy source code EXCEPT env.js
COPY . .

# This line is now optional but good for safety
RUN rm -f public/env.js

# Build app
RUN npm run build

# Stage 2 - Serve with NGINX
FROM nginx:alpine

# Remove default nginx content
RUN rm -rf /usr/share/nginx/html/*

# Copy build output
COPY --from=builder /app/build /usr/share/nginx/html

# ✅ Inject env.js at runtime
COPY public/env.js /usr/share/nginx/html/env.js

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
