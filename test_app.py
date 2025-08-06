from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/create_guide', methods=['POST'])
def create_guide():
    """Create a study guide - TEST VERSION"""
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        level = data.get('level', 'intermediate')
        focus_areas = data.get('focus_areas', '')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Mock response for testing
        mock_guide = f"""
        <div class="study-guide">
            <h3>📚 Study Guide: {topic}</h3>
            <p><strong>Level:</strong> {level.title()}</p>
            {f'<p><strong>Focus Areas:</strong> {focus_areas}</p>' if focus_areas else ''}
            
            <h4>🎯 Learning Objectives</h4>
            <ul>
                <li>Understand the fundamentals of {topic}</li>
                <li>Apply key concepts in practical scenarios</li>
                <li>Analyze complex problems related to {topic}</li>
            </ul>
            
            <h4>🔑 Key Concepts</h4>
            <ul>
                <li>Core principles and definitions</li>
                <li>Important theories and frameworks</li>
                <li>Real-world applications</li>
            </ul>
            
            <div class="alert alert-success mt-3">
                ✅ <strong>Test Success!</strong> Frontend-Backend connection is working properly!
            </div>
        </div>
        """
        
        return jsonify({'guide': mock_guide})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    """Generate practice questions - TEST VERSION"""
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        num_questions = int(data.get('num_questions', 5))
        question_types = data.get('question_types', ['multiple_choice'])
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Mock response for testing
        mock_questions = f"""
        <div class="practice-questions">
            <h3>❓ Practice Questions: {topic}</h3>
            <p><strong>Number of Questions:</strong> {num_questions}</p>
            <p><strong>Question Types:</strong> {', '.join(question_types)}</p>
            
            <div class="question-item mt-3">
                <h5>Question 1 (Multiple Choice)</h5>
                <p>What is a key concept in {topic}?</p>
                <ul>
                    <li>A) Option A</li>
                    <li>B) Option B</li>
                    <li>C) Option C</li>
                    <li>D) Option D</li>
                </ul>
            </div>
            
            <div class="alert alert-info mt-3">
                ✅ <strong>Test Success!</strong> Questions generation is working properly!
            </div>
        </div>
        """
        
        return jsonify({'questions': mock_questions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/explain_topic', methods=['POST'])
def explain_topic():
    """Explain a complex topic - TEST VERSION"""
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        difficulty_level = data.get('difficulty_level', 'beginner')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Mock response for testing
        mock_explanation = f"""
        <div class="topic-explanation">
            <h3>💡 Explanation: {topic}</h3>
            <p><strong>Difficulty Level:</strong> {difficulty_level.title()}</p>
            
            <h4>🔍 Simple Explanation</h4>
            <p>Here's a clear, step-by-step explanation of <strong>{topic}</strong> at the {difficulty_level} level:</p>
            
            <ol>
                <li><strong>Introduction:</strong> What is {topic} and why is it important?</li>
                <li><strong>Key Components:</strong> Breaking down the main parts</li>
                <li><strong>How it Works:</strong> Step-by-step process</li>
                <li><strong>Real-world Examples:</strong> Practical applications</li>
            </ol>
            
            <div class="alert alert-warning mt-3">
                ✅ <strong>Test Success!</strong> Topic explanation is working properly!
            </div>
        </div>
        """
        
        return jsonify({'explanation': mock_explanation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    """Summarize text - TEST VERSION"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        summary_type = data.get('summary_type', 'comprehensive')
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        # Mock response for testing
        word_count = len(text.split())
        mock_summary = f"""
        <div class="text-summary">
            <h3>📄 Text Summary</h3>
            <p><strong>Summary Type:</strong> {summary_type.title()}</p>
            <p><strong>Original Text Length:</strong> {word_count} words</p>
            
            <h4>📝 Summary</h4>
            <div class="summary-content">
                <p>This is a {summary_type} summary of your text. The original text contained {word_count} words and covered various topics.</p>
                
                <h5>Key Points:</h5>
                <ul>
                    <li>Main idea from the original text</li>
                    <li>Supporting arguments and evidence</li>
                    <li>Conclusions and implications</li>
                </ul>
            </div>
            
            <div class="alert alert-primary mt-3">
                ✅ <strong>Test Success!</strong> Text summarization is working properly!
            </div>
        </div>
        """
        
        return jsonify({'summary': mock_summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting Test Application...")
    print("📝 This is a test version with mock responses to verify frontend-backend connectivity")
    app.run(debug=True, host='0.0.0.0', port=5000)
