# Quick Start Guide for Adobe India Hackathon 2025

## System Verification ✅

Both Challenge_1a and Challenge_1b have been verified and are working correctly!

## Challenge_1a - PDF Outline Extraction

### Prerequisites
```bash
cd Challenge_1a
pip install -r requirements.txt
```

### Usage
```bash
# Basic usage with a PDF file
python3 extract_outline.py sample.pdf

# System will output JSON with extracted outline structure
```

### Features
- ✅ Multi-modal outline detection
- ✅ Ensemble classification system  
- ✅ Enhanced text processing
- ✅ Hierarchical structure extraction

## Challenge_1b - Persona-Driven Document Intelligence

### Prerequisites
```bash
cd Challenge_1b
# No additional dependencies needed (uses standard libraries)
```

### Usage
```bash
# Basic system (production ready)
python3 simple_persona_system.py --input input.json --output output.json

# Enhanced system with debugging
python3 enhanced_persona_system.py --input input.json --output output.json --debug

# Help for either system
python3 simple_persona_system.py --help
python3 enhanced_persona_system.py --help
```

### Input Format (input.json)
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_001",
    "test_case_name": "academic_research",
    "description": "Academic Research Analysis"
  },
  "documents": [
    {
      "filename": "document1.pdf",
      "title": "Document Title"
    }
  ],
  "persona": {
    "role": "PhD Researcher in Computational Biology"
  },
  "job_to_be_done": {
    "task": "Prepare a comprehensive literature review"
  }
}
```

### Features
- ✅ Enhanced persona analysis (6 persona types)
- ✅ Job-to-be-done optimization (5 job patterns)
- ✅ Advanced relevance scoring
- ✅ Multi-factor content analysis
- ✅ Hackathon-compliant output format

## Docker Deployment

Each challenge has its own Dockerfile:

```bash
# Challenge_1a
cd Challenge_1a
docker build -t challenge1a .
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output challenge1a

# Challenge_1b  
cd Challenge_1b
docker build -t challenge1b .
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output challenge1b
```

## System Test

Run the comprehensive test suite:
```bash
python3 test_systems.py
```

This verifies:
- ✅ Challenge_1a functionality
- ✅ Challenge_1b functionality  
- ✅ Docker configurations
- ✅ Documentation completeness

## Competition Readiness

Both systems are:
- ✅ **Functional**: All core features working
- ✅ **Compliant**: Output format matches hackathon requirements
- ✅ **Documented**: Comprehensive README files
- ✅ **Containerized**: Production-ready Docker configurations
- ✅ **Tested**: Comprehensive test suite passes

Ready for Adobe India Hackathon 2025 submission! 🏆
