# Stage 1: Build dependencies
FROM python:3.11-alpine AS builder

WORKDIR /app

# Install required system packages
RUN apk add --no-cache build-base

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final image
FROM python:3.11-alpine

WORKDIR /app

# Copy dependencies
COPY --from=builder /install /usr/local

# Copy application code
COPY app.py .

# Expose Flask default port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
