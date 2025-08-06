from flask import Flask, render_template, request, jsonify
from study_assistant import StudyAssistant
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Study Assistant
try:
    assistant = StudyAssistant()
    print("✅ Study Assistant initialized successfully!")
except Exception as e:
    print(f"❌ Error initializing Study Assistant: {str(e)}")
    assistant = None

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/study-guide')
def study_guide_page():
    return render_template('study_guide_page.html')

@app.route('/practice-questions')
def practice_questions_page():
    return render_template('practice_questions_page.html')

@app.route('/explain-topic')
def explain_topic_page():
    return render_template('explain_topic_page.html')

@app.route('/summarize')
def summarize_page():
    return render_template('summarize_page.html')

@app.route('/create_guide', methods=['POST'])
def create_guide():
    """Create a study guide"""
    if not assistant:
        return jsonify({'error': 'Study Assistant not available'}), 500
    
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        level = data.get('level', 'intermediate')
        focus_areas = data.get('focus_areas', '')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        guide = assistant.create_study_guide(topic, level, focus_areas if focus_areas else None)
        return jsonify({'guide': guide})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    """Generate practice questions"""
    if not assistant:
        return jsonify({'error': 'Study Assistant not available'}), 500
    
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        num_questions = int(data.get('num_questions', 5))
        question_types = data.get('question_types', ['multiple_choice', 'true_false', 'short_answer'])
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        questions = assistant.generate_practice_questions(topic, num_questions, question_types)
        return jsonify({'questions': questions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/explain_topic', methods=['POST'])
def explain_topic():
    """Explain a complex topic"""
    if not assistant:
        return jsonify({'error': 'Study Assistant not available'}), 500
    
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        difficulty_level = data.get('difficulty_level', 'beginner')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        explanation = assistant.explain_complex_topic(topic, difficulty_level)
        return jsonify({'explanation': explanation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    """Summarize text"""
    if not assistant:
        return jsonify({'error': 'Study Assistant not available'}), 500
    
    try:
        data = request.get_json()
        text = data.get('text', '')
        summary_type = data.get('summary_type', 'comprehensive')
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        summary = assistant.summarize_text(text, summary_type)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 