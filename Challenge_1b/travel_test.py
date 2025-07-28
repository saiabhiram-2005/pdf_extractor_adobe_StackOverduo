#!/usr/bin/env python3
"""
Travel-specific test for Enhanced Persona System
Tests the system with the actual travel planning scenario
"""

import json
import time
from enhanced_persona_system import EnhancedPersonaDocumentIntelligence

def run_travel_test():
    """Run a focused travel planning test"""
    print("🧳 TRAVEL PLANNING TEST")
    print("="*60)
    
    # Initialize system
    system = EnhancedPersonaDocumentIntelligence()
    
    # Travel planning scenario
    input_data = {
        "documents": [
            {"filename": "South of France - Cities.pdf", "title": "South of France - Cities"},
            {"filename": "South of France - Cuisine.pdf", "title": "South of France - Cuisine"},
            {"filename": "South of France - History.pdf", "title": "South of France - History"},
            {"filename": "South of France - Restaurants and Hotels.pdf", "title": "South of France - Restaurants and Hotels"},
            {"filename": "South of France - Things to Do.pdf", "title": "South of France - Things to Do"}
        ],
        "persona": {"role": "Travel Planner"},
        "job_to_be_done": {"task": "Plan a trip of 4 days for a group of 10 college friends."}
    }
    
    print(f"📋 Persona: {input_data['persona']['role']}")
    print(f"🎯 Task: {input_data['job_to_be_done']['task']}")
    print(f"📚 Documents: {len(input_data['documents'])} travel guides")
    print()
    
    # Process with enhanced system
    start_time = time.time()
    result = system.process_documents(input_data)
    processing_time = time.time() - start_time
    
    print("📊 RESULTS SUMMARY:")
    print("-" * 40)
    print(f"⏱️  Processing Time: {processing_time:.3f}s")
    print(f"🎯 Persona Confidence: {result['metadata']['persona_confidence']:.3f}")
    print(f"📋 Job Confidence: {result['metadata']['job_confidence']:.3f}")
    print(f"📄 Sections Extracted: {len(result['extracted_sections'])}")
    print(f"📝 Sub-sections: {len(result['subsection_analysis'])}")
    print()
    
    print("🏆 TOP 5 SECTIONS:")
    print("-" * 40)
    for i, section in enumerate(result['extracted_sections'][:5], 1):
        print(f"{i}. 📄 {section['document']}")
        print(f"   📝 {section['section_title'][:60]}...")
        print(f"   ⭐ Rank: {section['importance_rank']:.1f}")
        print()
    
    print("🔍 SAMPLE SUB-SECTIONS:")
    print("-" * 40)
    for i, subsection in enumerate(result['subsection_analysis'][:3], 1):
        print(f"{i}. 📄 {subsection['document']}")
        print(f"   📑 Page: {subsection['page_number_constraints']}")
        print(f"   📝 {subsection['refined_text'][:80]}...")
        print()
    
    # Save detailed results
    output_file = "travel_test_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Detailed results saved to: {output_file}")
    print("✅ Travel test completed!")

if __name__ == "__main__":
    run_travel_test()
