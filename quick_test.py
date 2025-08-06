#!/usr/bin/env python3
"""
Quick test script for Study Assistant
Run this to test the basic functionality
"""

from study_assistant import StudyAssistant

def test_study_assistant():
    """Test the Study Assistant functionality"""
    print("🎓 Testing Study Assistant...")
    print("=" * 50)
    
    try:
        # Initialize the assistant
        assistant = StudyAssistant()
        print("✅ Study Assistant initialized successfully!")
        
        # Test 1: Create a study guide
        print("\n📚 Test 1: Creating a study guide...")
        guide = assistant.create_study_guide("Python Programming", "beginner", "basics")
        print("✅ Study guide created!")
        print("📖 Sample from guide:")
        print(guide[:500] + "..." if len(guide) > 500 else guide)
        
        # Test 2: Generate practice questions
        print("\n❓ Test 2: Generating practice questions...")
        questions = assistant.generate_practice_questions("Machine Learning", 3)
        print("✅ Practice questions generated!")
        print("📝 Sample questions:")
        print(questions[:500] + "..." if len(questions) > 500 else questions)
        
        # Test 3: Explain a complex topic
        print("\n💡 Test 3: Explaining a complex topic...")
        explanation = assistant.explain_complex_topic("Neural Networks", "beginner")
        print("✅ Topic explained!")
        print("🧠 Sample explanation:")
        print(explanation[:500] + "..." if len(explanation) > 500 else explanation)
        
        # Test 4: Summarize text
        print("\n📋 Test 4: Summarizing text...")
        sample_text = """
        Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines that work and react like humans. 
        Some of the activities computers with artificial intelligence are designed for include speech recognition, learning, planning, and problem solving. 
        AI has been used in various applications such as virtual assistants, autonomous vehicles, medical diagnosis, and game playing. 
        Machine learning, a subset of AI, enables computers to learn and improve from experience without being explicitly programmed. 
        Deep learning, a type of machine learning, uses neural networks with multiple layers to analyze various factors of data.
        """
        summary = assistant.summarize_text(sample_text, "comprehensive")
        print("✅ Text summarized!")
        print("📄 Summary:")
        print(summary[:500] + "..." if len(summary) > 500 else summary)
        
        print("\n🎉 All tests completed successfully!")
        print("✅ Study Assistant is working properly!")
        
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    test_study_assistant() 