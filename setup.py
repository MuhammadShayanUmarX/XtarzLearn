#!/usr/bin/env python3
"""
Setup script for Study Assistant
Helps users configure the application quickly
"""

import os
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        os.system("pip install -r requirements.txt")
        print("✅ Dependencies installed successfully!")
        return True
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def create_env_file():
    """Create .env file with API key prompt"""
    env_file = Path(".env")
    
    if env_file.exists():
        print("✅ .env file already exists!")
        return True
    
    print("\n🔑 Setting up API key...")
    print("You need a Google Gemini API key to use this application.")
    print("Get your API key from: https://makersuite.google.com/app/apikey")
    
    api_key = input("\nEnter your Google Gemini API key: ").strip()
    
    if not api_key:
        print("❌ API key is required!")
        return False
    
    try:
        with open(".env", "w") as f:
            f.write(f"GOOGLE_API_KEY={api_key}\n")
        print("✅ .env file created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def test_setup():
    """Test the setup by running a quick test"""
    print("\n🧪 Testing setup...")
    try:
        from study_assistant import StudyAssistant
        assistant = StudyAssistant()
        print("✅ Study Assistant initialized successfully!")
        
        # Quick test
        test_result = assistant.explain_complex_topic("Python Programming", "beginner")
        if test_result and not test_result.startswith("Error"):
            print("✅ API connection working!")
            return True
        else:
            print("❌ API test failed!")
            return False
    except Exception as e:
        print(f"❌ Setup test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🎓 Study Assistant Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Create .env file
    if not create_env_file():
        return
    
    # Test setup
    if not test_setup():
        print("\n❌ Setup failed! Please check your API key and try again.")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n🚀 You can now run the Study Assistant:")
    print("   • Web interface: python app.py")
    print("   • Command line: python study_assistant.py")
    print("   • Quick test: python quick_test.py")
    print("\n📖 For more information, see README.md")

if __name__ == "__main__":
    main() 