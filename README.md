# XtarzLearn - AI-Powered Study Assistant

![XtarzLearn Logo](static/logo-1.png)

A comprehensive educational platform powered by Google's Gemini API. XtarzLearn helps students and learners create study guides, generate practice questions, explain complex topics, and summarize long texts with an intuitive, modern interface.

## 🚀 Features

### 1. Study Guide Generator
- Create structured study guides with clear learning objectives
- Generate key concepts and detailed explanations
- Include relevant examples and applications
- Export guides for offline use

### 2. Practice Questions
- Generate custom practice questions based on any topic
- Multiple question types (multiple choice, true/false, short answer)
- Difficulty level customization
- Instant feedback and explanations

### 3. Topic Explainer
- Break down complex topics into easy-to-understand explanations
- Adjust explanation depth based on your needs
- Get step-by-step breakdowns of difficult concepts
- Visual aids and examples for better understanding

### 4. Text Summarizer
- Condense long articles and documents into key points
- Adjust summary length based on your needs
- Extract main ideas and supporting details
- Save and organize your summaries

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend**: Python 3.7+
- **Web Framework**: Flask
- **AI Integration**: Google Gemini API
- **Styling**: Custom CSS with modern UI/UX principles
- **Responsive Design**: Works on desktop and mobile devices

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd week3
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 🏗️ Project Structure

```
week3/
├── static/                 # Static files (CSS, JS, images)
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # Image assets
├── templates/             # HTML templates
│   ├── components/        # Reusable components
│   ├── sections/          # Page sections
│   └── base.html          # Base template
├── .env                   # Environment variables
├── .gitignore             # Git ignore file
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
└── study_assistant.py     # AI integration module
```

## 🌟 Features in Detail

### Modern UI/UX
- Clean, responsive design that works on all devices
- Smooth animations and transitions
- Intuitive navigation and user flow
- Accessible and keyboard-navigable interface

### Study Guide Generator
- Input any topic and get a structured study guide
- Customize the depth and breadth of content
- Export guides as PDF or Markdown
- Save your favorite guides for later reference

### Practice Questions
- Generate unlimited practice questions
- Multiple difficulty levels
- Detailed explanations for each answer
- Track your progress over time

### Topic Explainer
- Get clear, concise explanations of complex topics
- Adjust the technical level of explanations
- See related concepts and topics
- Save explanations for future reference

### Text Summarizer
- Summarize articles, research papers, and documents
- Adjust summary length and detail level
- Extract key points and main ideas
- Organize your summaries by subject or project

## 🔒 Security

- API keys are stored in environment variables (never committed to version control)
- Secure API communication using HTTPS
- Input validation and sanitization
- Rate limiting to prevent abuse

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request with a clear description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google for the Gemini API
- Bootstrap for the responsive design framework
- All open-source libraries and tools used in this project
- Provide summary sections and practice questions
- Recommend additional resources

### 2. Generate Practice Questions
- Multiple choice questions with explanations
- True/False questions with reasoning
- Short answer questions with sample answers
- Essay questions with key points
- Problem-solving questions for math/science

### 3. Explain Complex Topics
- Break down difficult concepts into simple terms
- Use real-world analogies and examples
- Provide step-by-step explanations
- Address common misconceptions
- Include visual descriptions

### 4. Summarize Long Texts
- Create concise summaries of articles and documents
- Extract main points and key ideas
- Organize information logically
- Provide bullet points for easy reading
- Include key takeaways

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Google Gemini API key

### Installation

1. **Clone or download the project files**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up your API key:**
   - Create a `.env` file in the project directory
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your-api-key-here
     ```

### Usage

#### Option 1: Web Interface (Recommended)
```bash
python app.py
```
Then open your browser and go to `http://localhost:5000`

#### Option 2: Command Line Interface
```bash
python study_assistant.py
```

#### Option 3: Quick Test
```bash
python quick_test.py
```

## 📁 Project Structure

```
week 3/
├── study_assistant.py      # Main Study Assistant class
├── app.py                  # Flask web application
├── quick_test.py          # Quick test script
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/
│   └── index.html         # Web interface template
└── .env                   # Environment variables (create this)
```

## 🎨 Web Interface Features

The web interface provides a beautiful, modern UI with:

- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Processing**: Live feedback during AI generation
- **Multiple Formats**: Support for different question types and summary styles
- **User-friendly Interface**: Intuitive forms and clear results display

### Web Interface Screenshots

The interface includes four main sections:
1. **Create Study Guide** - Generate comprehensive study materials
2. **Generate Practice Questions** - Create various types of questions
3. **Explain Complex Topic** - Break down difficult concepts
4. **Summarize Text** - Condense long articles and documents

## 🔧 API Usage Examples

### Create a Study Guide
```python
from study_assistant import StudyAssistant

assistant = StudyAssistant()
guide = assistant.create_study_guide(
    topic="Machine Learning",
    level="intermediate",
    focus_areas="neural networks, algorithms"
)
print(guide)
```

### Generate Practice Questions
```python
questions = assistant.generate_practice_questions(
    topic="Python Programming",
    num_questions=5,
    question_types=["multiple_choice", "true_false"]
)
print(questions)
```

### Explain a Complex Topic
```python
explanation = assistant.explain_complex_topic(
    topic="Quantum Computing",
    difficulty_level="beginner"
)
print(explanation)
```

### Summarize Text
```python
summary = assistant.summarize_text(
    text="Your long text here...",
    summary_type="comprehensive"
)
print(summary)
```

## 🛠️ Configuration

### Environment Variables
Create a `.env` file with:
```
GOOGLE_API_KEY=your-gemini-api-key-here
```

### Customization
You can modify the system prompts in `study_assistant.py` to customize:
- Study guide structure
- Question generation style
- Explanation approach
- Summary format

## 🎓 Educational Use Cases

### For Students
- Create study guides for exam preparation
- Generate practice questions for self-assessment
- Understand complex topics through simplified explanations
- Summarize lengthy research papers

### For Teachers
- Generate teaching materials
- Create assessment questions
- Develop lesson plans
- Prepare study resources

### For Researchers
- Summarize academic papers
- Generate research questions
- Explain complex theories
- Create literature reviews

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file exists and contains the correct API key
   - Verify the API key is valid and has proper permissions

2. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.7+ required)

3. **Web Interface Not Loading**
   - Ensure Flask is installed
   - Check if port 5000 is available
   - Try accessing `http://127.0.0.1:5000` instead

4. **Slow Response Times**
   - This is normal for AI generation
   - Complex topics may take longer to process
   - Check your internet connection

## 📚 Supported Topics

The Study Assistant can handle a wide range of subjects:

- **Computer Science**: Programming, Algorithms, Data Structures
- **Mathematics**: Calculus, Algebra, Statistics
- **Sciences**: Physics, Chemistry, Biology
- **Humanities**: History, Literature, Philosophy
- **Languages**: Grammar, Vocabulary, Translation
- **Business**: Economics, Marketing, Management
- **And many more...**

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the UI/UX
- Enhancing the AI prompts
- Adding support for more educational content types

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Google Gemini API for providing the AI capabilities
- Flask framework for the web interface
- Bootstrap for the responsive design

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Verify your API key and internet connection
3. Try the quick test script to isolate issues

---

**Happy Learning! 🎓✨** "# XtarzLearn_" 
