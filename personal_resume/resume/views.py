from pathlib import Path
from django.shortcuts import render

def resume_view(request):
    # Check if a custom photo exists, else fallback to SVG avatar
    static_dir = Path(__file__).resolve().parent / 'static' / 'resume'
    photo = 'resume/profile.svg'
    for ext in ['profile.jpg', 'profile.png', 'profile.jpeg']:
        if (static_dir / ext).exists():
            photo = f'resume/{ext}'
            break

    data = {
        'name': 'Nikhil Krishna R D',
        'title': 'AI/ML Engineer | Data Analyst',
        'profile_photo': photo,
        'personal_info': {
            'Location': 'Coimbatore, Tamil Nadu',
            'Phone': '8825895654',
            'Email': 'rdnikhilkrishna2004@gmail.com',
        },
        'contact': {
            'Phone': '8825895654',
            'Email': 'rdnikhilkrishna2004@gmail.com',
            'Location': 'Coimbatore, Tamil Nadu',
            'LinkedIn': 'https://www.linkedin.com/in/nikhil-krishna-r-d-773b84259/',
            'GitHub': 'https://github.com/rdnk2004',
            'Portfolio': 'https://rdnkportfolio.vercel.app',
        },
        'career_objective': (
            'To build a career in Artificial Intelligence, Machine Learning, and Data Analytics '
            'by developing reliable, data-driven solutions to real-world problems. I aim to apply my '
            'expertise in machine learning, data analysis, automation, and software development '
            'while continuously exploring emerging technologies and contributing to impactful projects.'
        ),
        'education': [
            {
                'degree': 'Master of Science, Computer Science (Data Analytics)',
                'institution': 'Rajagiri College of Social Sciences',
                'duration': 'June 2025 – March 2027',
                'score': 'GPA: 8.02 / 10',
            },
            {
                'degree': 'Bachelor of Science, Data Science',
                'institution': 'Kumaraguru College of Liberal Arts and Science',
                'duration': 'August 2022 – June 2025',
                'score': 'GPA: 9.022 / 10',
            },
        ],
        'skills': {
            'Machine Learning': [
                'Python', 'XGBoost', 'SHAP', 'Prophet', 'ResNet-50', 'scikit-learn', 'Pandas', 'NumPy'
            ],
            'MLOps & Deployment': [
                'MLflow', 'Docker', 'FastAPI', 'Flask', 'CI/CD'
            ],
            'Data Engineering & Analytics': [
                'SQL', 'PostgreSQL', 'MongoDB', 'Pandera', 'Power BI'
            ],
            'Tools & Technologies': [
                'Git', 'Playwright', 'Excel Automation', 'Gemini API (LLM)'
            ],
        },
        'experience': [
            {
                'role': 'Web Developer',
                'company': 'RLabZ',
                'duration': 'November 2025 – Present',
                'location': 'Rajagiri College',
                'responsibilities': [
                    'Building the official website for an international academic conference at Rajagiri College, expected to host 300+ attendees.',
                    'Managing frontend architecture, production deployment, and CI/CD pipelines.',
                    'Collaborating with design and content teams to maintain institutional branding standards.',
                ],
            },
            {
                'role': 'Automation and Platform Developer',
                'company': 'Kumaraguru College of Liberal Arts and Science',
                'duration': 'December 2024 – March 2025',
                'location': 'Coimbatore',
                'responsibilities': [
                    'Developed an automated DOCX report-generation system, reducing generation time from 1–2 hours to under 30 seconds.',
                    'Built a marklist processing platform for 1,400+ students across 12 departments, reducing processing time from over 2 hours to under 2 minutes.',
                    'Developed real-time result-analysis dashboards with role-based access for Admin, HOD, and Faculty users.',
                ],
            },
            {
                'role': 'Data Analyst Intern',
                'company': 'CAI Mahindra',
                'duration': 'July 2024 – August 2024',
                'location': 'Coimbatore',
                'responsibilities': [
                    'Analyzed the ETBR sales funnel to identify conversion drop-off patterns.',
                    'Automated 15+ recurring Excel reports, reducing report-generation time by 97%.',
                    'Developed and deployed a Flask-based internal KPI dashboard for self-service sales analytics.',
                ],
            },
        ],
        'projects': [
            {
                'title': "Supply vs. Demand Drivers of India's CPI Inflation",
                'duration': 'June 2026 – July 2026',
                'tech': 'XGBoost, SHAP, STL Decomposition, Prophet, LLM Evaluation, Python',
                'points': [
                    'Analyzed 10 years of RBI Monetary Policy Committee decisions and CPI data.',
                    'Applied STL decomposition and stationarity-corrected Granger causality.',
                    'Built an XGBoost + SHAP pipeline using walk-forward cross-validation.',
                    'Used LLM-based text comparison to validate model rationale against RBI minutes.',
                    'Backtested Prophet forecasting confidence intervals.',
                ],
            },
            {
                'title': 'Nexus Task-Tracker',
                'duration': 'January 2026 – February 2026',
                'tech': 'FastAPI, PostgreSQL, Docker, Nginx, JWT, Kanban',
                'points': [
                    'Developed a multi-user project management application with JWT authentication and Kanban workflows.',
                    'Built REST APIs using FastAPI and PostgreSQL.',
                    'Implemented role-based task access and task lifecycle validation.',
                    'Containerized and deployed the application using Docker and Nginx.',
                ],
            },
            {
                'title': 'Anomaly Detection Using ResNet-50',
                'duration': 'December 2024 – February 2025',
                'tech': 'ResNet-50, Transfer Learning, Flask, Data Augmentation',
                'points': [
                    'Developed a ResNet-50 transfer-learning pipeline for industrial defect classification.',
                    'Achieved 94% accuracy on hazelnut defects and 87% on bottle defects.',
                    'Applied data augmentation, early stopping, and learning-rate scheduling.',
                    'Deployed real-time defect inference and visualization through Flask.',
                ],
            },
        ],
        'certifications': [
            'Oracle Cloud Infrastructure 2025 – Certified Data Science Professional (Oracle University)',
            'Applied Data Science with Python – Level 2 (IBM)',
            'Database Management Essentials (Honors) (University of Colorado, Coursera)',
        ],
        'achievements': [
            'University 3rd Rank — Bachelor of Science in Data Science',
            'Best Student Award — Data Science',
            'Mahatma Gandhi Merit Scholarship — 3 Times Recipient',
            'Published researcher in a UGC CARE-listed journal',
        ],
        'languages': [
            'English',
            'Malayalam',
        ],
        'hobbies': [
            'Coding & Software Development',
            'Artificial Intelligence & Machine Learning',
            'Data Analytics',
            'Exploring Emerging Technologies',
            'Building Real-World Applications',
            'Academic Research',
            'Filmmaking & Creative Projects',
        ],
    }
    return render(request, 'resume/index.html', {'resume': data})
