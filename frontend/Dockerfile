# Simple Dockerfile for React Frontend
FROM node:18-alpine

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy all frontend source files
COPY public/ ./public/
COPY src/ ./src/

# Build the React app
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
