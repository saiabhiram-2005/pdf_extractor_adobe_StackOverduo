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

# Copy the main scripts
COPY extract_outline.py .
COPY persona_document_intelligence.py .

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Make the scripts executable
RUN chmod +x extract_outline.py persona_document_intelligence.py

# Set environment variables for offline operation
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the default command to process PDFs with persona-driven intelligence
CMD ["python", "persona_document_intelligence.py", "--persona", "researcher", "--job", "literature review"]