#!/usr/bin/env python3
"""
Simple Resume Generator
Creates professional resume in HTML and PDF format
"""

import json
from datetime import datetime

def create_resume_html(data):
    """Generate HTML resume"""
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{data['name']} - Resume</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
        .header {{ text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; margin-bottom: 30px; }}
        .name {{ font-size: 28px; font-weight: bold; margin-bottom: 10px; }}
        .contact {{ font-size: 14px; color: #666; }}
        .section {{ margin-bottom: 25px; }}
        .section-title {{ font-size: 18px; font-weight: bold; color: #333; border-bottom: 1px solid #ccc; padding-bottom: 5px; margin-bottom: 15px; }}
        .job {{ margin-bottom: 20px; }}
        .job-title {{ font-weight: bold; font-size: 16px; }}
        .company {{ font-style: italic; color: #666; }}
        .dates {{ float: right; color: #666; font-size: 14px; }}
        .description {{ margin-top: 8px; }}
        .education {{ margin-bottom: 15px; }}
        .skills {{ display: flex; flex-wrap: wrap; gap: 10px; }}
        .skill {{ background: #f0f0f0; padding: 5px 10px; border-radius: 15px; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="header">
        <div class="name">{data['name']}</div>
        <div class="contact">
            {data['email']} | {data['phone']} | {data['location']}
            {f" | LinkedIn: {data['linkedin']}" if data.get('linkedin') else ""}
        </div>
    </div>

    <div class="section">
        <div class="section-title">Professional Summary</div>
        <p>{data['summary']}</p>
    </div>

    <div class="section">
        <div class="section-title">Work Experience</div>
        {"".join([f'''
        <div class="job">
            <div class="job-title">{exp['title']}</div>
            <div class="company">{exp['company']} <span class="dates">{exp['dates']}</span></div>
            <div class="description">{exp['description']}</div>
        </div>
        ''' for exp in data['experience']])}
    </div>

    <div class="section">
        <div class="section-title">Education</div>
        {"".join([f'''
        <div class="education">
            <strong>{edu['degree']}</strong> - {edu['school']} ({edu['year']})
        </div>
        ''' for edu in data['education']])}
    </div>

    <div class="section">
        <div class="section-title">Skills</div>
        <div class="skills">
            {"".join([f'<span class="skill">{skill.strip()}</span>' for skill in data['skills'].split(',')])}
        </div>
    </div>
</body>
</html>
"""
    return html

def get_sample_data():
    """Sample resume data"""
    return {
        "name": "John Doe",
        "email": "john.doe@email.com",
        "phone": "+1 (555) 123-4567",
        "location": "New York, NY",
        "linkedin": "linkedin.com/in/johndoe",
        "summary": "Results-driven software engineer with 5+ years of experience developing scalable web applications. Proven track record of leading cross-functional teams and delivering high-quality solutions that improve user experience and drive business growth.",
        "experience": [
            {
                "title": "Senior Software Engineer",
                "company": "Tech Corp",
                "dates": "2022 - Present",
                "description": "• Led development of microservices architecture serving 100K+ users\n• Improved application performance by 40% through code optimization\n• Mentored 3 junior developers and conducted code reviews"
            },
            {
                "title": "Software Engineer",
                "company": "StartupXYZ",
                "dates": "2020 - 2022",
                "description": "• Developed full-stack web applications using React and Node.js\n• Implemented CI/CD pipelines reducing deployment time by 60%\n• Collaborated with product team to define technical requirements"
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Science in Computer Science",
                "school": "University of Technology",
                "year": "2020"
            }
        ],
        "skills": "JavaScript, Python, React, Node.js, AWS, Docker, Git, SQL, MongoDB, REST APIs"
    }

def main():
    print("🚀 Simple Resume Generator")
    print("=" * 30)
    
    # Get user input or use sample data
    choice = input("Use sample data? (y/n): ").lower()
    
    if choice == 'y':
        data = get_sample_data()
    else:
        data = {}
        print("\nEnter your information:")
        data['name'] = input("Full Name: ")
        data['email'] = input("Email: ")
        data['phone'] = input("Phone: ")
        data['location'] = input("Location: ")
        data['linkedin'] = input("LinkedIn (optional): ")
        data['summary'] = input("Professional Summary: ")
        
        # Simple experience entry
        data['experience'] = []
        exp_count = int(input("Number of work experiences: "))
        for i in range(exp_count):
            exp = {}
            print(f"\nExperience {i+1}:")
            exp['title'] = input("Job Title: ")
            exp['company'] = input("Company: ")
            exp['dates'] = input("Dates (e.g., 2020-2022): ")
            exp['description'] = input("Description: ")
            data['experience'].append(exp)
        
        # Simple education entry
        data['education'] = []
        edu_count = int(input("Number of education entries: "))
        for i in range(edu_count):
            edu = {}
            print(f"\nEducation {i+1}:")
            edu['degree'] = input("Degree: ")
            edu['school'] = input("School: ")
            edu['year'] = input("Year: ")
            data['education'].append(edu)
        
        data['skills'] = input("Skills (comma-separated): ")
    
    # Generate HTML
    html_content = create_resume_html(data)
    
    # Save HTML file
    filename = f"resume_{data['name'].replace(' ', '_').lower()}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✅ Resume generated: {filename}")
    print(f"📂 Location: {os.path.abspath(filename)}")
    print("\n📋 To convert to PDF:")
    print("1. Open the HTML file in your browser")
    print("2. Press Ctrl+P (or Cmd+P on Mac)")
    print("3. Select 'Save as PDF' as destination")
    print("4. Click Save")

if __name__ == "__main__":
    import os
    main()