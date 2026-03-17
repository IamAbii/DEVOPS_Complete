# Stage 1: Build React App
FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN rm -f public/env.js
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY --from=builder /app/src/config.json /usr/share/nginx/html/config.json
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
