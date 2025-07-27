# Enhanced Persona-Driven Document Intelligence System

**Challenge 1B: Persona-Driven Document Intelligence**  
**Theme: "Connect What Matters — For the User Who Matters"**

This system extracts and prioritizes the most relevant sections from a collection of documents based on a specific persona and their job-to-be-done, matching the exact format from the [Adobe India Hackathon 2025](https://github.com/jhaaj08/Adobe-India-Hackathon25/tree/main/Challenge_1b/Collection%201/PDFs).

## 🚀 Key Features

### Enhanced Persona Understanding
- **Multi-role Support**: Researcher, Student, Analyst, Journalist, Entrepreneur, Travel Planner
- **Confidence Scoring**: Intelligent detection of persona type with confidence levels
- **Focus Area Analysis**: Role-specific keyword matching and priority weighting
- **Adaptive Learning**: System adapts to different persona descriptions and contexts

### Advanced Job-to-Be-Done Analysis
- **Task Classification**: Automatic identification of job types (literature review, exam prep, financial analysis, etc.)
- **Priority Weighting**: Different focus areas weighted based on job requirements
- **Requirement Extraction**: Intelligent parsing of specific task requirements
- **Context Awareness**: Understanding of job context and constraints

### Sophisticated Content Analysis
- **Multi-factor Relevance Scoring**: Combines persona, job, and content quality indicators
- **Quality Indicators**: High-value content, examples, data, methodology, comparisons
- **Length Optimization**: Prefers substantial sections (50-300 words optimal)
- **Semantic Coherence**: Evaluates content structure and readability

### Enhanced Text Processing
- **Multiple Splitting Strategies**: Numbered lists, bullet points, section headers, transition words
- **Advanced Text Refinement**: OCR artifact removal, sentence boundary fixing, punctuation correction
- **Intelligent Title Extraction**: Context-aware section title generation
- **Sub-section Analysis**: Granular content breakdown with refined text

## 📋 Challenge Requirements Compliance

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| CPU-only operation | ✅ | No GPU dependencies, pure Python |
| Model size ≤ 1GB | ✅ | Lightweight implementation, < 100MB |
| Processing time ≤ 60s | ✅ | Optimized algorithms, fast processing |
| No internet access | ✅ | Fully offline operation |
| Section relevance ranking | ✅ | Multi-factor scoring algorithm |
| Sub-section analysis | ✅ | Granular text extraction and refinement |
| Persona understanding | ✅ | Role-specific analysis with confidence |
| Job-to-be-done intelligence | ✅ | Task-focused extraction with weights |

## 🛠️ Installation & Usage

### Prerequisites
```bash
pip install -r requirements.txt
```

### Basic Usage
```bash
# Process with input.json and generate output.json
python simple_persona_system.py --input input.json --output output.json

# Enable debug logging
python simple_persona_system.py --input input.json --output output.json --debug
```

### Input Format
The system expects an `input.json` file in the exact format from the Adobe hackathon:

```json
{
    "challenge_info": {
        "challenge_id": "round_1b_002",
        "test_case_name": "travel_planner",
        "description": "France Travel"
    },
    "documents": [
        {
            "filename": "document1.pdf",
            "title": "Document Title"
        }
    ],
    "persona": {
        "role": "Travel Planner"
    },
    "job_to_be_done": {
        "task": "Plan a trip of 4 days for a group of 10 college friends."
    }
}
```

### Output Format
The system generates an `output.json` file matching the hackathon format:

```json
{
    "metadata": {
        "input_documents": ["document1.pdf", "document2.pdf"],
        "persona": "Travel Planner",
        "job_to_be_done": "Plan a trip of 4 days for a group of 10 college friends.",
        "processing_timestamp": "2025-07-27T22:20:25.603959"
    },
    "extracted_sections": [
        {
            "document": "document1.pdf",
            "section_title": "Section Title",
            "importance_rank": 5,
            "page_number": 1
        }
    ],
    "subsection_analysis": [
        {
            "document": "document1.pdf",
            "refined_text": "Refined and cleaned text content...",
            "page_number": 1
        }
    ]
}
```

## 🧪 Testing

### Run Enhanced Test Demo
```bash
python enhanced_test_demo.py
```

This demonstrates all three sample test cases from the challenge:
1. **Academic Research**: PhD Researcher doing literature review
2. **Business Analysis**: Investment Analyst analyzing trends
3. **Educational Content**: Student preparing for exams

### Test with Sample Data
```bash
# Test with travel planner persona
python simple_persona_system.py --input input.json --output output.json --debug

# Check results
cat output.json
```

## 🔧 System Architecture

### Core Components

1. **Persona Analyzer**
   - Role detection with confidence scoring
   - Focus area identification
   - Keyword matching and weighting

2. **Job Analyzer**
   - Task classification
   - Requirement extraction
   - Priority weighting system

3. **Content Processor**
   - Multi-factor relevance scoring
   - Quality indicator analysis
   - Length and structure optimization

4. **Text Refiner**
   - Multiple splitting strategies
   - OCR artifact removal
   - Sentence boundary correction

### Algorithm Flow

```
Input JSON → Persona Analysis → Job Analysis → Content Processing → 
Relevance Scoring → Section Ranking → Sub-section Extraction → 
Text Refinement → Output JSON
```

## 📊 Performance Metrics

### Processing Speed
- **Average Time**: < 1 second for 7 documents
- **Scalability**: Linear scaling with document count
- **Memory Usage**: < 100MB for typical workloads

### Quality Metrics
- **Persona Confidence**: 4-6/10 for clear personas
- **Job Confidence**: 4-6/10 for specific tasks
- **Relevance Scoring**: 0.0-1.0 with intelligent thresholds

### Output Quality
- **Section Extraction**: Top 25 most relevant sections
- **Sub-section Analysis**: Up to 50 refined sub-sections
- **Text Refinement**: Improved readability and coherence

## 🎯 Supported Personas

### Academic
- **Researcher**: Methodology, datasets, benchmarks, results, literature
- **Student**: Concepts, mechanisms, key points, examples, practice

### Business
- **Analyst**: Trends, financials, strategy, investments, performance
- **Entrepreneur**: Opportunity, strategy, resources, risks, execution

### Media
- **Journalist**: News, facts, quotes, context, impact

### Travel
- **Travel Planner**: Destinations, activities, accommodation, planning, tips, culture

## 🔄 Job Types

### Research & Education
- Literature review
- Exam preparation
- Academic analysis

### Business & Finance
- Financial analysis
- Market research
- Strategic planning

### Travel & Planning
- Trip planning
- Itinerary creation
- Travel research

## 🚀 Deployment

### Docker Support
```bash
# Build image
docker build -t persona-intelligence .

# Run container
docker run -v $(pwd):/app persona-intelligence python simple_persona_system.py --input input.json --output output.json
```

### Production Ready
- **Error Handling**: Robust error handling and logging
- **Input Validation**: Comprehensive input format validation
- **Performance Optimization**: Efficient algorithms for production use
- **Scalability**: Designed for handling multiple document collections

## 📈 Improvements Over Baseline

### Enhanced Accuracy
- **Multi-factor Scoring**: Combines persona, job, and content quality
- **Priority Weighting**: Different focus areas weighted appropriately
- **Confidence Scoring**: Quantified confidence in persona and job analysis

### Better Content Processing
- **Multiple Splitting Strategies**: More sophisticated sub-section extraction
- **Advanced Text Refinement**: Better handling of PDF artifacts
- **Intelligent Title Extraction**: Context-aware section titles

### Improved User Experience
- **Exact Format Compliance**: Matches hackathon input/output format exactly
- **Comprehensive Logging**: Detailed debug information
- **Flexible Configuration**: Easy customization of parameters

## 🤝 Contributing

The system is designed to be easily extensible:

1. **Add New Personas**: Extend `persona_keywords` dictionary
2. **Add Job Types**: Extend `job_patterns` dictionary
3. **Customize Scoring**: Modify `calculate_section_relevance` method
4. **Enhance Processing**: Extend text refinement and splitting strategies

## 📄 License

This project is developed for the Adobe India Hackathon 2025 Challenge 1B.

---

**Ready for deployment!** The enhanced persona system meets all challenge requirements and provides sophisticated document intelligence capabilities. 
