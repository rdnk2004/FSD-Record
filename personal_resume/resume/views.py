from django.shortcuts import render

def resume_view(request):
    data = {
        'name': 'Alex Morgan',
        'title': 'Full Stack Developer & Computer Science Student',
        'personal_info': {
            'Date of Birth': '15 August 2004',
            'Gender': 'Male',
            'Nationality': 'Indian',
            'Location': 'Chennai, Tamil Nadu, India',
        },
        'contact': {
            'Email': 'alex.morgan@example.com',
            'Phone': '+91 98765 43210',
            'LinkedIn': 'linkedin.com/in/alexmorgan',
            'GitHub': 'github.com/alexmorgan',
            'Portfolio': 'alexmorgan.dev',
        },
        'career_objective': (
            'Motivated Computer Science undergraduate seeking an entry-level software engineering '
            'or full-stack developer role to leverage skills in Python, Django, and modern web '
            'technologies while contributing to impactful software solutions.'
        ),
        'education': [
            {
                'degree': 'B.Tech in Computer Science and Engineering',
                'institution': 'ABC Institute of Technology',
                'duration': '2022 - 2026',
                'score': 'CGPA: 8.8 / 10.0',
            },
            {
                'degree': 'Higher Secondary Certificate (HSC)',
                'institution': 'St. Mary’s Higher Secondary School',
                'duration': '2020 - 2022',
                'score': 'Percentage: 92.4%',
            },
            {
                'degree': 'Secondary School Leaving Certificate (SSLC)',
                'institution': 'St. Mary’s Matriculation School',
                'duration': '2019 - 2020',
                'score': 'Percentage: 94.0%',
            },
        ],
        'skills': {
            'Programming Languages': ['Python', 'C', 'C++', 'Java', 'JavaScript'],
            'Web Technologies': ['HTML5', 'CSS3', 'Django', 'REST APIs', 'Bootstrap'],
            'Databases': ['SQLite', 'MySQL', 'PostgreSQL'],
            'Tools & Platforms': ['Git', 'GitHub', 'VS Code', 'Linux', 'Postman'],
            'Soft Skills': ['Problem Solving', 'Team Collaboration', 'Effective Communication', 'Time Management'],
        },
        'experience': [
            {
                'role': 'Web Development Intern',
                'company': 'TechSphere Solutions',
                'duration': 'June 2025 - August 2025',
                'location': 'Remote',
                'responsibilities': [
                    'Assisted in building responsive frontend interfaces using HTML5, CSS3, and JavaScript.',
                    'Integrated Django REST API endpoints with the database and improved query performance.',
                    'Participated in code reviews and collaborated with senior developers using Git.',
                ],
            },
        ],
        'projects': [
            {
                'title': 'Online Flight Booking System',
                'tech': 'Python, Django, SQLite, HTML5, CSS3',
                'description': 'Developed a full-stack flight reservation system featuring flight search, real-time seat availability tracking, ticket booking, and booking cancellation.',
            },
            {
                'title': 'Student Course Registration Portal',
                'tech': 'Django Framework, Bootstrap, SQLite',
                'description': 'Built an academic course registration portal allowing students to enroll in departmental courses with prerequisite validation and credit limits.',
            },
            {
                'title': 'Interactive Bill & Invoice Generator',
                'tech': 'JavaScript, HTML5, CSS3',
                'description': 'Created a dynamic invoice calculation utility with automatic tax computation, discount deduction, and print-ready bill rendering.',
            },
        ],
        'certifications': [
            'Python for Everybody Specialization - Coursera / University of Michigan',
            'Full Stack Web Development with Django - Udemy',
            'Foundations of Cybersecurity - Google Career Certificates',
        ],
        'achievements': [
            '1st Place in Inter-College Web Designing Hackathon (CodeFest 2025)',
            'Completed 150+ coding problems on LeetCode & GeeksforGeeks',
            'Awarded Merit Scholarship for Academic Excellence (2023 - 2024)',
        ],
        'languages': [
            {'name': 'English', 'proficiency': 'Professional Working Proficiency'},
            {'name': 'Tamil', 'proficiency': 'Native / Bilingual'},
            {'name': 'Hindi', 'proficiency': 'Conversational'},
        ],
        'hobbies': [
            'Open Source Contributing',
            'Competitive Coding',
            'Chess',
            'Tech Blogging',
            'Photography',
        ],
    }
    return render(request, 'resume/index.html', {'resume': data})
