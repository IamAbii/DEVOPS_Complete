# Use a smaller Alpine-based Python image
FROM python:3.11-alpine as builder

# Set the working directory
WORKDIR /app

# Install dependencies first (to leverage Docker caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Create a lightweight runtime image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy only necessary files
COPY --from=builder /install /usr/local
COPY app.py .

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
