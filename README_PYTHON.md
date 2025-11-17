# AI-Powered Resume Builder (Python/Streamlit Version)

A comprehensive AI-powered resume building and optimization system built with Streamlit, featuring real AI enhancement using OpenAI and Gemini APIs.

## Features

- **Dual Input Methods**: File upload (PDF/DOCX) and manual entry
- **ATS Scoring System**: Comprehensive scoring with detailed breakdown
- **Real AI Enhancement**: Content improvement using OpenAI GPT and Google Gemini
- **Professional Templates**: Multiple template options
- **Multi-format Export**: PDF and Word document generation
- **Score Improvement Tracking**: Before/after ATS score comparison
- **Interactive AI Chat**: Resume improvement assistant

## Quick Start

### 1. Install Dependencies

```bash
# Option 1: Use setup script
python setup.py

# Option 2: Manual installation
pip install -r requirements.txt
```

### 2. Set API Keys

Create a `.env` file or set environment variables:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export GEMINI_API_KEY="your-gemini-api-key"
```

### 3. Run the Application

```bash
streamlit run resume_builder_app.py
```

## Dependencies

- `streamlit` - Web application framework
- `openai` - OpenAI API client
- `google-generativeai` - Google Gemini API client
- `python-docx` - Word document generation
- `reportlab` - PDF generation
- `PyPDF2` - PDF text extraction
- `docx2txt` - DOCX text extraction

## Usage

1. **Input Resume Data**: Choose between file upload or manual entry
2. **ATS Score Analysis**: Get detailed scoring and recommendations
3. **AI Enhancement**: Let AI improve your resume content
4. **Generate Documents**: Create professional PDF and Word documents

## API Configuration

### OpenAI API
- Get your API key from [OpenAI Platform](https://platform.openai.com/)
- Used for content enhancement and chat assistance

### Google Gemini API
- Get your API key from [Google AI Studio](https://makersuite.google.com/)
- Used as fallback for content enhancement

## File Structure

```
ats/
├── resume_builder_app.py    # Main Streamlit application
├── requirements.txt         # Python dependencies
├── setup.py                # Setup script
├── README_PYTHON.md        # This file
└── index.html              # HTML version (separate)
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **API Errors**: Check your API keys are set correctly
   ```bash
   echo $OPENAI_API_KEY
   echo $GEMINI_API_KEY
   ```

3. **PDF Generation Issues**: Install reportlab
   ```bash
   pip install reportlab
   ```

4. **Word Generation Issues**: Install python-docx
   ```bash
   pip install python-docx
   ```

### Error Messages

- **"PDF generation not available"**: Install reportlab
- **"Word generation not available"**: Install python-docx
- **"File processing not available"**: Install PyPDF2 and docx2txt
- **"API Error"**: Check your API keys and internet connection

## Features in Detail

### ATS Scoring Algorithm
- **Contact Information** (20 points): Name, email, phone, location, LinkedIn, portfolio
- **Work Experience** (30 points): Job titles, companies, detailed descriptions
- **Education** (20 points): Degrees, institutions
- **Skills & Keywords** (30 points): Relevant technical and soft skills

### AI Enhancement
- **Summary Enhancement**: Professional tone, quantified achievements, keywords
- **Experience Enhancement**: Action verbs, STAR format, metrics
- **Skills Enhancement**: Industry-relevant technologies, organized categories

### Document Generation
- **PDF**: Professional formatting using ReportLab
- **Word**: Native .docx format using python-docx
- **Templates**: Modern, Executive, and Creative styles

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review error messages carefully
3. Ensure all dependencies are installed
4. Verify API keys are configured correctly

## Version History

- **v1.0**: Initial release with core functionality
- **v1.1**: Added AI enhancement and chat features
- **v1.2**: Improved error handling and documentation