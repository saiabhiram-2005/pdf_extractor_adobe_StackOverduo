# Project Organization Guide

## Overview

This repository is organized into two separate challenges, each with its own dedicated folder and complete set of files for easy navigation and deployment.

## Directory Structure

```
pdf_extractor/
├── README.md                    # Main project overview
├── PROJECT_ORGANIZATION.md      # This file
├── requirements.txt             # Legacy requirements (can be removed)
├── Dockerfile                   # Legacy Dockerfile (can be removed)
├── challenge1a/                 # Challenge 1A: PDF Outline Extraction
│   ├── extract_outline.py       # Main PDF processing script
│   ├── Dockerfile              # Challenge 1A specific Dockerfile
│   ├── requirements.txt        # Challenge 1A dependencies
│   └── README.md               # Challenge 1A documentation
└── challenge1b/                 # Challenge 1B: Persona-Driven Document Intelligence
    ├── simple_persona_system.py # Simplified working version
    ├── persona_document_intelligence.py # Full version (has dependencies)
    ├── approach_explanation.md  # Methodology explanation
    ├── README_CHALLENGE.md      # Challenge 1B documentation
    ├── challenge1b_output.json  # Sample output format
    ├── test_persona_system.py   # Test script with sample cases
    ├── Dockerfile              # Challenge 1B specific Dockerfile
    └── requirements.txt        # Challenge 1B dependencies
```

## Challenge 1A: PDF Outline Extraction

**Location**: `challenge1a/`

**Purpose**: Extract structured outlines (headings, titles, page numbers) from PDF documents.

**Key Files**:
- `extract_outline.py` - Main processing script with advanced PDF analysis
- `Dockerfile` - Container configuration for deployment
- `requirements.txt` - Dependencies (pdfminer.six)
- `README.md` - Detailed documentation and usage instructions

**Quick Start**:
```bash
cd challenge1a
docker build -t pdf-outline-extractor .
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-outline-extractor
```

## Challenge 1B: Persona-Driven Document Intelligence

**Location**: `challenge1b/`

**Purpose**: Extract and prioritize relevant sections from document collections based on specific personas and their job-to-be-done.

**Key Files**:
- `simple_persona_system.py` - **RECOMMENDED**: Working version without complex dependencies
- `persona_document_intelligence.py` - Full version (requires working extract_outline.py)
- `approach_explanation.md` - 300-500 word methodology explanation
- `README_CHALLENGE.md` - Comprehensive challenge documentation
- `challenge1b_output.json` - Sample output format
- `test_persona_system.py` - Test script with all three sample cases
- `Dockerfile` - Container configuration for deployment
- `requirements.txt` - Dependencies

**Quick Start**:
```bash
cd challenge1b
python simple_persona_system.py --persona "PhD Researcher" --job "literature review"
```

## File Descriptions

### Challenge 1A Files

| File | Description |
|------|-------------|
| `extract_outline.py` | Advanced PDF processing with multi-modal heading detection |
| `Dockerfile` | Container configuration for Challenge 1A |
| `requirements.txt` | Python dependencies |
| `README.md` | Challenge 1A documentation |

### Challenge 1B Files

| File | Description |
|------|-------------|
| `simple_persona_system.py` | **Primary script** - Working persona-driven system |
| `persona_document_intelligence.py` | Full version with PDF integration |
| `approach_explanation.md` | Methodology explanation (300-500 words) |
| `README_CHALLENGE.md` | Comprehensive challenge documentation |
| `challenge1b_output.json` | Sample output in required format |
| `test_persona_system.py` | Test script with sample cases |
| `Dockerfile` | Container configuration for Challenge 1B |
| `requirements.txt` | Python dependencies |

## Usage Recommendations

### For Challenge 1A
Use the files in `challenge1a/` directory. This is a complete, working solution for PDF outline extraction.

### For Challenge 1B
**Primary Recommendation**: Use `simple_persona_system.py` in the `challenge1b/` directory. This is a working, self-contained solution that demonstrates the persona-driven approach without complex dependencies.

**Alternative**: Use `persona_document_intelligence.py` if you have a working version of `extract_outline.py` (the original has some indentation issues that need to be resolved).

## Testing

### Challenge 1A Testing
```bash
cd challenge1a
python extract_outline.py file03.pdf
```

### Challenge 1B Testing
```bash
cd challenge1b
python test_persona_system.py
```

Or test individual cases:
```bash
python simple_persona_system.py --persona "PhD Researcher" --job "literature review"
python simple_persona_system.py --persona "Investment Analyst" --job "financial analysis"
python simple_persona_system.py --persona "Student" --job "exam preparation"
```

## Docker Deployment

### Challenge 1A
```bash
cd challenge1a
docker build -t challenge1a .
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output challenge1a
```

### Challenge 1B
```bash
cd challenge1b
docker build -t challenge1b .
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output challenge1b
```

## Output Files

### Challenge 1A
- Generates JSON files in `output/` directory
- One output file per input PDF
- Contains title, outline, and processing metrics

### Challenge 1B
- Generates `challenge1b_output.json` in the current directory
- Contains metadata, extracted sections, and sub-section analysis
- Follows the exact format specified in the challenge requirements

## Legacy Files

The following files in the root directory are legacy and can be removed:
- `requirements.txt` (root)
- `Dockerfile` (root)

These have been replaced by challenge-specific versions in their respective directories.

## Support

Each challenge has its own complete documentation and can be deployed independently. The separation allows for:
- Independent development and testing
- Clear separation of concerns
- Easy deployment and maintenance
- Focused documentation for each challenge 