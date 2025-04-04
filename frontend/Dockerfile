# Use a builder stage to install dependencies
FROM node:20-alpine as builder
WORKDIR /app

# Copy only package.json (ignore package-lock.json)
COPY package.json ./
RUN npm install --only=production

# Copy the entire source code
COPY . .

# Final production image
FROM node:20-alpine
WORKDIR /app

# Copy necessary files from the builder stage
COPY --from=builder /app /app

EXPOSE 3000
CMD ["npm", "start"]
