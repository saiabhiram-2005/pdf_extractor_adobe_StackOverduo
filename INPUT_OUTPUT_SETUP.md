# PDF Document Intelligence Solutions - Input/Output Setup

## Directory Structure for Testing

After cloning the repository, you'll need to set up input directories and add your documents:

### Challenge 1A Setup
```bash
cd Challenge_1a
mkdir input
# Add your PDF files to input/ directory
# Example: cp your-document.pdf input/
```

### Challenge 1B Setup  
```bash
cd Challenge_1b
mkdir input
# Add your document collection to input/ directory
# Copy and modify input.json.example to input.json with your configuration
```

## Sample Files

This directory contains example configurations and will be populated with your test documents.

### Input Format Examples
- `input.json.example` - Sample input configuration for Challenge 1B
- PDF files should be placed in the `input/` directory

### Expected Output
- Challenge 1A: JSON files with extracted outlines
- Challenge 1B: JSON files with persona-driven section analysis

## Getting Started

1. Create input directories: `mkdir input`
2. Add your PDF documents 
3. For Challenge 1B: Copy `input.json.example` to `input.json` and customize
4. Run the Docker containers or Python scripts
5. Check output/ directory for results
