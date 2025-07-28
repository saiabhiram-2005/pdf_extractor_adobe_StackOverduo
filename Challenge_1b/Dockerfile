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

# Copy all necessary Python files
COPY enhanced_persona_system.py .
COPY simple_persona_system.py .
COPY comprehensive_test_demo.py .
COPY enhanced_test_demo.py .
COPY sample_test.py .
COPY travel_test.py .
COPY input.json .

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Make scripts executable
RUN chmod +x enhanced_persona_system.py
RUN chmod +x simple_persona_system.py
RUN chmod +x comprehensive_test_demo.py

# Set environment variables for offline operation
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the default command to run the enhanced persona system
# Use the enhanced system for production deployment
CMD ["python", "enhanced_persona_system.py", "--input", "input.json", "--output", "output.json"] 