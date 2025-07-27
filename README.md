# PDF Document Intelligence Challenges

This repository contains solutions for two related document intelligence challenges:

## Project Structure

```
pdf_extractor/
├── challenge1a/          # Challenge 1A: PDF Outline Extraction
│   ├── extract_outline.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
├── challenge1b/          # Challenge 1B: Persona-Driven Document Intelligence
│   ├── simple_persona_system.py
│   ├── persona_document_intelligence.py
│   ├── approach_explanation.md
│   ├── README_CHALLENGE.md
│   ├── challenge1b_output.json
│   ├── test_persona_system.py
│   ├── Dockerfile
│   └── requirements.txt
└── README.md            # This file
```

## Challenge Overview

### Challenge 1A: PDF Outline Extraction
**Goal**: Extract structured outlines (headings, titles, page numbers) from PDF documents.

**Key Features**:
- Multi-modal heading detection using font characteristics, positioning, and semantic patterns
- Robust title extraction with multiple fallback strategies
- Multilingual support (English, Spanish, French, German, Japanese, Chinese, Russian)
- Font-agnostic detection for challenge compliance
- Performance optimized (< 10 seconds for 50-page PDFs)

**Technical Requirements**:
- ✅ CPU-only operation
- ✅ Model size < 200MB
- ✅ AMD64 architecture support
- ✅ Offline operation (no internet access)

### Challenge 1B: Persona-Driven Document Intelligence
**Theme**: "Connect What Matters — For the User Who Matters"

**Goal**: Extract and prioritize relevant sections from document collections based on specific personas and their job-to-be-done.

**Key Features**:
- **Persona Understanding**: Researcher, Student, Analyst, Journalist, Entrepreneur
- **Job-to-Be-Done Intelligence**: Literature review, exam preparation, financial analysis, market research
- **Intelligent Section Ranking**: Relevance scoring based on persona and job requirements
- **Sub-Section Analysis**: Granular text extraction and refinement
- **Multi-Document Synthesis**: Comparative analysis across document collections

**Technical Requirements**:
- ✅ CPU-only operation
- ✅ Model size < 1GB
- ✅ Processing time ≤ 60 seconds for 3-5 documents
- ✅ Offline operation (no internet access)

## Quick Start

### Challenge 1A: PDF Outline Extraction

```bash
cd challenge1a

# Build Docker image
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .

# Run with PDF files
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:latest
```

### Challenge 1B: Persona-Driven Document Intelligence

```bash
cd challenge1b

# Build Docker image
docker build --platform linux/amd64 -t persona-doc-intelligence:latest .

# Run with sample test case
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  persona-doc-intelligence:latest \
  --persona "PhD Researcher in Computational Biology" \
  --job "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"
```

## Sample Test Cases

### Challenge 1B Test Cases

#### Test Case 1: Academic Research
- **Documents**: 4 research papers on "Graph Neural Networks for Drug Discovery"
- **Persona**: PhD Researcher in Computational Biology
- **Job**: "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"

#### Test Case 2: Business Analysis
- **Documents**: 3 annual reports from competing tech companies (2022-2024)
- **Persona**: Investment Analyst
- **Job**: "Analyze revenue trends, R&D investments, and market positioning strategies"

#### Test Case 3: Educational Content
- **Documents**: 5 chapters from organic chemistry textbooks
- **Persona**: Undergraduate Chemistry Student
- **Job**: "Identify key concepts and mechanisms for exam preparation on reaction kinetics"

## Innovation Highlights

### Challenge 1A Innovations
- **Multi-Modal Heading Detection**: Combines font characteristics, positioning, semantic patterns, and visual hierarchy
- **Ensemble Approach**: Multiple lightweight classifiers for improved accuracy
- **Robust Title Extraction**: Multiple fallback strategies for challenging documents
- **Language-Agnostic Processing**: Handles diverse document formats and languages

### Challenge 1B Innovations
- **Persona-Aware Processing**: Understands user roles and tailors extraction accordingly
- **Job-Specific Intelligence**: Prioritizes content based on specific task requirements
- **Multi-Document Synthesis**: Provides comparative insights across document collections
- **Granular Sub-Section Analysis**: Detailed breakdowns for deeper insights

## Performance Benchmarks

### Challenge 1A
| PDF Size | Pages | Processing Time | Memory Usage |
|----------|-------|-----------------|--------------|
| Small    | 1-10  | < 2 seconds     | < 100MB      |
| Medium   | 11-25 | 2-5 seconds     | < 150MB      |
| Large    | 26-50 | 5-10 seconds    | < 200MB      |

### Challenge 1B
| Document Count | Processing Time | Memory Usage |
|----------------|-----------------|--------------|
| 3-5 documents  | < 30 seconds    | < 500MB      |
| 6-8 documents  | < 45 seconds    | < 800MB      |
| 9-10 documents | < 60 seconds    | < 1GB        |

## Architecture Comparison

| Feature | Challenge 1A | Challenge 1B |
|---------|--------------|--------------|
| **Focus** | Structural extraction | Semantic understanding |
| **Input** | Single PDF | Multiple PDFs |
| **Output** | Outline structure | Relevant sections + ranking |
| **Intelligence** | Pattern recognition | Persona-driven analysis |
| **Complexity** | Medium | High |

## Development

### Local Development

#### Challenge 1A
```bash
cd challenge1a
pip install -r requirements.txt
python extract_outline.py file03.pdf
```

#### Challenge 1B
```bash
cd challenge1b
pip install -r requirements.txt
python simple_persona_system.py --persona "researcher" --job "literature review"
```

### Testing
Both challenges include comprehensive test suites and sample data for validation.

## License

These solutions are designed for the PDF Document Intelligence Challenges. 