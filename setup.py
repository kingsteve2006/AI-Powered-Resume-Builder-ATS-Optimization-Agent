#!/usr/bin/env python3
"""
Setup script for AI Resume Builder
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True

def setup_environment():
    """Setup environment variables"""
    print("\n🔧 Setting up environment...")
    print("Please set your API keys as environment variables:")
    print("export OPENAI_API_KEY='your-openai-api-key'")
    print("export GEMINI_API_KEY='your-gemini-api-key'")
    print("\nOr create a .env file with:")
    print("OPENAI_API_KEY=your-openai-api-key")
    print("GEMINI_API_KEY=your-gemini-api-key")

def main():
    print("🚀 Setting up AI Resume Builder...")
    
    if install_requirements():
        setup_environment()
        print("\n✅ Setup complete!")
        print("Run the application with: streamlit run resume_builder_app.py")
    else:
        print("\n❌ Setup failed. Please check the error messages above.")

if __name__ == "__main__":
    main()