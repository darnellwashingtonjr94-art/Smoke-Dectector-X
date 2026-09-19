FROM python:3.10-slim

# Install system dependencies for OpenCV and hardware GPIO
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and config
COPY src/ src/
COPY config.yaml .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the main script
CMD ["python", "src/main.py"]
