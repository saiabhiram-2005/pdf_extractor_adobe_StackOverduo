FROM --platform=linux/amd64 python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies (minimal, no GPU dependencies)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies (no network calls during runtime)
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY Challenge_1a/ ./Challenge_1a/
COPY Challenge_1b/ ./Challenge_1b/
COPY PROJECT_ORGANIZATION.md .
COPY README.md .

# Create input and output directories for both challenges
RUN mkdir -p /app/input /app/output \
    /app/Challenge_1a/input /app/Challenge_1a/output \
    /app/Challenge_1b/input /app/Challenge_1b/output

# Set environment variables for offline operation
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Default command shows available options
CMD ["echo", "PDF Document Intelligence Solutions - Use specific challenge Docker images:\n- Challenge_1a: docker build -t pdf-outline-extractor ./Challenge_1a\n- Challenge_1b: docker build -t persona-intelligence ./Challenge_1b"]