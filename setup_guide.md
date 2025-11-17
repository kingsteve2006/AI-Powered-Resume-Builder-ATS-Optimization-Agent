# AI-Powered Resume Builder - Python Setup & Deployment Guide

## Overview
This is a Python-based AI-Powered Resume Builder built with Streamlit that provides the same functionality as the HTML version but with enhanced capabilities and real AI integration.

## Features
- **Streamlit Web Interface**: Modern, responsive web UI
- **Real OpenAI & Gemini APIs**: Authentic AI enhancement
- **Dual Input Methods**: File upload and manual entry
- **ATS Scoring System**: Comprehensive scoring with breakdown
- **Document Generation**: PDF and Word export
- **Interactive AI Chat**: Real-time resume advice
- **Step-by-Step Workflow**: Guided user experience

## Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenAI API key (provided)
- Gemini API key (provided)

## Installation Steps

### 1. Clone or Download Files
```bash
# Download the following files:
# - resume_builder_app.py
# - requirements.txt
# - setup_guide.md
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit openai google-generativeai python-docx reportlab PyPDF2 docx2txt
```

### 3. Run the Application
```bash
streamlit run resume_builder_app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy directly from GitHub repository

### Option 2: Heroku Deployment

**Procfile:**
```
web: streamlit run resume_builder_app.py --server.port=$PORT --server.address=0.0.0.0
```

**requirements.txt:** (already provided)

**runtime.txt:**
```
python-3.9.16
```

### Option 3: Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "resume_builder_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Build and run:**
```bash
docker build -t resume-builder .
docker run -p 8501:8501 resume-builder
```

## API Configuration

### OpenAI Integration
- **Model**: GPT-3.5-turbo
- **Purpose**: Primary AI enhancement provider
- **Features**: Summary enhancement, experience optimization, skills expansion

### Gemini Integration
- **Model**: Gemini-1.5-flash-latest
- **Purpose**: Backup AI enhancement provider
- **Features**: Fallback AI enhancement when OpenAI fails

## Core Components

### 1. ResumeData Class
Handles resume information structure and validation.

### 2. ATSScorer Class
- Contact Information: 20 points
- Work Experience: 30 points
- Education: 20 points
- Skills: 30 points

### 3. AIEnhancer Class
- Real OpenAI/Gemini API integration
- Fallback enhancement algorithms
- Chat assistant functionality

### 4. DocumentGenerator Class
- PDF generation using ReportLab
- Word document creation using python-docx
- Multiple template support

## Usage Workflow

1. **Input**: Choose file upload or manual entry
2. **Form Completion**: Fill in personal info, experience, education
3. **ATS Analysis**: Get scoring breakdown and recommendations
4. **AI Enhancement**: Real AI-powered content improvement
5. **Template Selection**: Choose from 3 professional templates
6. **Document Generation**: Download PDF and/or Word formats

## Advanced Features

### Interactive Chat Assistant
- Real-time AI advice
- Context-aware responses
- ATS optimization tips

### Score Improvement Tracking
- Before/after score comparison
- Visual progress indicators
- Detailed improvement metrics

### Template Preview
- Real-time template preview
- Side-by-side comparison
- Professional formatting

## Troubleshooting

### Common Issues

**Import Errors:**
```bash
# Install missing dependencies
pip install -r requirements.txt
```

**API Key Issues:**
- Ensure OpenAI API key is valid
- Check Gemini API key configuration
- Monitor API usage and rate limits

**Port Conflicts:**
```bash
# Use different port
streamlit run resume_builder_app.py --server.port 8502
```

### Performance Optimization
- Enable caching for API responses
- Optimize large file uploads
- Monitor memory usage for document generation

## Security Considerations

### API Key Management
- Store API keys as environment variables in production
- Never commit API keys to version control
- Use secure deployment platforms

### File Upload Security
- Validate file types and sizes
- Sanitize uploaded content
- Implement rate limiting

## Support and Maintenance

### Updates and Patches
- Monitor Streamlit updates
- Update API libraries periodically
- Review and enhance scoring algorithms

### Performance Monitoring
- Track user engagement
- Monitor API usage and costs
- Analyze conversion metrics

## File Structure
```
resume-builder/
├── resume_builder_app.py     # Main application
├── requirements.txt          # Dependencies
├── setup_guide.md           # This guide
├── README.md                # Project documentation
└── .streamlit/              # Optional: Streamlit configuration
    └── config.toml          # Custom Streamlit settings
```

## Next Steps

### Feature Enhancements
- Multi-language support
- Advanced template library
- Integration with job boards
- Automated job posting analysis

### Technical Improvements
- Database integration
- User authentication
- Resume versioning
- Collaborative editing

---

This Python implementation provides a robust, scalable solution for AI-powered resume building with professional-grade features and real AI integration.