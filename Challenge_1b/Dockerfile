FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the enhanced persona system
COPY simple_persona_system.py .
COPY enhanced_test_demo.py .

# Make scripts executable
RUN chmod +x simple_persona_system.py
RUN chmod +x enhanced_test_demo.py

# Set default command to run the enhanced persona system
# This will process input.json and generate output.json
CMD ["python", "simple_persona_system.py", "--input", "input.json", "--output", "output.json"] 