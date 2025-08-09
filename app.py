from flask import Flask, render_template, request, jsonify
from study_assistant import StudyAssistant
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure upload settings
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'doc'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@app.route('/assignment-input')
def assignment_input_page():
    return render_template('assignment_input_page.html')

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

@app.route('/submit_assignment', methods=['POST'])
def submit_assignment():
    """Handle assignment form submission"""
    if not assistant:
        return jsonify({'error': 'Study Assistant not available'}), 500
    
    try:
        # Get form data
        assignment_name = request.form.get('assignment_name', '')
        details = request.form.get('details', '')
        output_format = request.form.get('output_format', 'Report')
        word_count = request.form.get('word_count', '')
        
        if not assignment_name or not details:
            return jsonify({'error': 'Assignment name and details are required'}), 400
        
        # Handle file upload
        uploaded_files = []
        if 'reference_files' in request.files:
            files = request.files.getlist('reference_files')
            for file in files:
                if file and file.filename != '' and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    uploaded_files.append(filename)
        
        # Read reference files content if any
        reference_content = ""
        if uploaded_files:
            for filename in uploaded_files:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        reference_content += f"\n\n--- Content from {filename} ---\n"
                        reference_content += f.read()
                except Exception as e:
                    reference_content += f"\n\n--- Error reading {filename}: {str(e)} ---\n"
        
        # Generate the assignment using the proper method
        result = assistant.generate_assignment(
            assignment_name=assignment_name,
            details=details,
            output_format=output_format,
            word_count=word_count,
            reference_content=reference_content
        )
        
        return jsonify({
            'success': True,
            'assignment_name': assignment_name,
            'output_format': output_format,
            'result': result,
            'uploaded_files': uploaded_files
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 