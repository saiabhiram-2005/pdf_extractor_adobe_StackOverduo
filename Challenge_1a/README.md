# PDF Outline Extractor

A robust PDF outline extraction solution that automatically detects titles, headings, and page numbers from PDF documents using advanced multi-modal heuristics.

## Features

- ✅ **Multi-page PDF support** (up to 50+ pages)
- ✅ **Table of Contents handling** (prevents duplication)
- ✅ **High heading detection accuracy** using ensemble approach
- ✅ **Performance optimized** (< 10 seconds for 50-page PDFs)
- ✅ **Multilingual support** (English, Spanish, French, German, Japanese, Chinese, Russian)
- ✅ **Font-agnostic detection** (works without relying on font size)
- ✅ **Robust title extraction** with multiple fallback strategies
- ✅ **OCR corruption handling** for scanned documents
- ✅ **Semantic duplicate removal** to prevent redundant headings
- ✅ **Offline operation** (no network calls during runtime)

## Docker Requirements Compliance

- ✅ **AMD64 Architecture**: Explicitly specified with `--platform=linux/amd64`
- ✅ **No GPU Dependencies**: CPU-only operation
- ✅ **Model Size**: < 200MB (uses lightweight pdfminer.six library)
- ✅ **Offline Operation**: No internet calls during runtime
- ✅ **Performance**: ≤ 10 seconds for 50-page PDFs
- ✅ **Resource Usage**: Optimized for 8 CPUs and 16GB RAM

## Quick Start

### Build the Docker Image

```bash
docker build --platform linux/amd64 -t pdf-extractor:latest .
```

### Run the Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-extractor:latest
```

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Process a single PDF
python extract_outline.py file03.pdf
```

## Input/Output Format

### Input
- Place PDF files in the `input/` directory
- Supported formats: PDF (any version)

### Output
- JSON files generated in the `output/` directory
- One `filename.json` per `filename.pdf`

### Output Format
```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Main Heading",
      "page": 1
    },
    {
      "level": "H2", 
      "text": "Sub Heading",
      "page": 2
    }
  ],
  "processing_time": 2.04,
  "performance_metrics": {
    "total_elements": 1500,
    "headings_found": 25,
    "time_per_page": 0.04,
    "detected_language": "en"
  }
}
```

## Technical Architecture

### Multi-Modal Heading Detection
The solution uses an ensemble approach combining:
1. **Font characteristics** (size, weight, family)
2. **Positional context** (indentation, spacing)
3. **Semantic patterns** (keywords, structure)
4. **Visual hierarchy** (whitespace, alignment)
5. **Sequential patterns** (numbered lists, chapters)
6. **Font-agnostic detection** (challenge requirement)

### Robust Title Extraction
Multiple fallback strategies:
1. RFP-specific extraction for proposal documents
2. Largest font size detection
3. First page content analysis
4. Document metadata patterns
5. Common title patterns
6. Filename-based extraction

### Performance Optimizations
- Efficient text extraction using pdfminer.six
- Early filtering of non-heading content
- Optimized regex patterns
- Minimal memory footprint
- Parallel processing where possible

## Supported Languages

- **English**: Primary language with extensive keyword support
- **Spanish**: Introducción, resumen, conclusión, etc.
- **French**: Introduction, résumé, conclusion, etc.
- **German**: Einleitung, zusammenfassung, schlussfolgerung, etc.
- **Japanese**: はじめに, 概要, 結論, etc.
- **Chinese**: 介绍, 概述, 结论, etc.
- **Russian**: Введение, резюме, заключение, etc.

## Error Handling

- Graceful fallback for corrupted PDFs
- OCR corruption detection and filtering
- Invalid font handling
- Memory-efficient processing
- Comprehensive error logging

## Performance Benchmarks

| PDF Size | Pages | Processing Time | Memory Usage |
|----------|-------|-----------------|--------------|
| Small    | 1-10  | < 2 seconds     | < 100MB      |
| Medium   | 11-25 | 2-5 seconds     | < 150MB      |
| Large    | 26-50 | 5-10 seconds    | < 200MB      |

## Constraints Compliance

- ✅ **Execution Time**: ≤ 10 seconds for 50-page PDFs
- ✅ **Model Size**: < 200MB (pdfminer.six: ~15MB)
- ✅ **Network**: No internet access required
- ✅ **Runtime**: CPU-only (AMD64), optimized for 8 CPUs, 16GB RAM
- ✅ **Architecture**: Explicitly targets linux/amd64 platform

## Troubleshooting

### Common Issues

1. **Permission Denied**: Ensure input/output directories are writable
2. **Memory Issues**: Solution is optimized for 16GB RAM
3. **Performance**: Processing time scales linearly with PDF size
4. **OCR Quality**: Handles corrupted text automatically

### Debug Mode

For local development, enable debug logging:
```python
extractor = PDFOutlineExtractor(debug=True)
```

## License

This solution is designed for the PDF Outline Extraction Challenge.
