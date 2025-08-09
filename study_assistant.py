import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Load prompts from prompts.json
with open("prompts.json", "r", encoding="utf-8") as f:
    PROMPTS = json.load(f)

class StudyAssistant:
    def __init__(self):
        """Initialize the Study Assistant with Gemini API"""
        self.api_key = os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        self.system_prompt = PROMPTS["system_prompt"]
    
    def create_study_guide(self, topic, level="intermediate", focus_areas=None):
        """Create a comprehensive study guide for a given topic"""
        prompt = PROMPTS["study_guide_prompt"].format(
            topic=topic,
            level=level,
            focus_areas=focus_areas if focus_areas else 'comprehensive coverage'
        )
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"<div class='alert alert-danger'>Error creating study guide: {str(e)}</div>"
    
    def generate_practice_questions(self, topic, num_questions=5, question_types=None):
        """Generate practice questions for a given topic"""
        if question_types is None:
            question_types = ["multiple_choice", "true_false", "short_answer"]
        prompt = PROMPTS["practice_questions_prompt"].format(
            topic=topic,
            num_questions=num_questions,
            question_types=", ".join(question_types)
        )
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"<div class='alert alert-danger'>Error generating practice questions: {str(e)}</div>"
    
    def explain_complex_topic(self, topic, difficulty_level="beginner"):
        """Explain a complex topic in simple terms"""
        prompt = PROMPTS["explain_topic_prompt"].format(
            topic=topic,
            difficulty_level=difficulty_level
        )
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"<div class='alert alert-danger'>Error explaining topic: {str(e)}</div>"
    
    def summarize_text(self, text, summary_type="comprehensive"):
        """Summarize long text or content"""
        prompt = PROMPTS["summarize_text_prompt"].format(
            text=text,
            summary_type=summary_type
        )
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"<div class='alert alert-danger'>Error summarizing text: {str(e)}</div>"
    
    def generate_assignment(self, assignment_name, details, output_format="Report", word_count="", reference_content=""):
        """Generate a custom assignment based on user requirements"""
        prompt = PROMPTS["assignment_prompt"].format(
            assignment_name=assignment_name,
            details=details,
            output_format=output_format,
            word_count=word_count if word_count else "No specific length requirement",
            reference_content=reference_content if reference_content else "No reference files provided"
        )
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"<div class='alert alert-danger'>Error generating assignment: {str(e)}</div>"
    
    def interactive_study_session(self):
        """Run an interactive study session"""
        print("🎓 Welcome to Study Assistant!")
        print("=" * 50)
        print("Available features:")
        print("1. Create Study Guide")
        print("2. Generate Practice Questions")
        print("3. Explain Complex Topic")
        print("4. Summarize Text")
        print("5. Exit")
        print("=" * 50)
        
        while True:
            try:
                choice = input("\n📚 Choose an option (1-5): ").strip()
                
                if choice == "1":
                    topic = input("📖 Enter the topic for study guide: ")
                    level = input("📊 Enter level (beginner/intermediate/advanced) [default: intermediate]: ") or "intermediate"
                    focus = input("🎯 Enter focus areas (optional): ")
                    
                    print("\n🔄 Creating study guide...")
                    guide = self.create_study_guide(topic, level, focus if focus else None)
                    print("\n📚 STUDY GUIDE:")
                    print("=" * 50)
                    print(guide)
                    
                elif choice == "2":
                    topic = input("❓ Enter the topic for practice questions: ")
                    num = input("🔢 Number of questions [default: 5]: ") or "5"
                    types = input("📝 Question types (multiple_choice/true_false/short_answer/essay) [default: all]: ") or "all"
                    
                    print("\n🔄 Generating practice questions...")
                    questions = self.generate_practice_questions(topic, int(num))
                    print("\n❓ PRACTICE QUESTIONS:")
                    print("=" * 50)
                    print(questions)
                    
                elif choice == "3":
                    topic = input("🤔 Enter the complex topic to explain: ")
                    level = input("📊 Difficulty level (beginner/intermediate/advanced) [default: beginner]: ") or "beginner"
                    
                    print("\n🔄 Explaining topic...")
                    explanation = self.explain_complex_topic(topic, level)
                    print("\n💡 EXPLANATION:")
                    print("=" * 50)
                    print(explanation)
                    
                elif choice == "4":
                    print("📝 Enter the text to summarize (press Enter twice when done):")
                    lines = []
                    while True:
                        line = input()
                        if line == "":
                            break
                        lines.append(line)
                    
                    text = "\n".join(lines)
                    if text.strip():
                        summary_type = input("📊 Summary type (comprehensive/brief/key_points) [default: comprehensive]: ") or "comprehensive"
                        
                        print("\n🔄 Summarizing text...")
                        summary = self.summarize_text(text, summary_type)
                        print("\n📋 SUMMARY:")
                        print("=" * 50)
                        print(summary)
                    else:
                        print("❌ No text provided for summarization.")
                        
                elif choice == "5":
                    print("👋 Thank you for using Study Assistant! Good luck with your studies!")
                    break
                    
                else:
                    print("❌ Invalid choice. Please select 1-5.")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")

def main():
    """Main function to run the Study Assistant"""
    try:
        assistant = StudyAssistant()
        print("✅ Study Assistant initialized successfully!")
        assistant.interactive_study_session()
    except Exception as e:
        print(f"❌ Error initializing Study Assistant: {str(e)}")
        print("Please make sure your GOOGLE_API_KEY is set in the .env file")

if __name__ == "__main__":
    main() 