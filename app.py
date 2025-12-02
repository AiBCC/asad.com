from flask import Flask, render_template, request, flash, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Sample data for portfolio
SKILLS = {
    'Technical Skills': [
        'MySQL Database',
        'Python for Analysis',
        'Microsoft Power BI ',
        'Tableau Public',
        'Microsoft Excel',
        'Looker Studio',
    ],
    'Business Skills': [
        'Requirements Gathering',
        'Stakeholder Communication',
        'Data Analysis & Interpretation',
        'Statistical Analysis',
        'KPI Development',
        'Data Storytelling'
    ]
}

PROJECTS = [
    {
        'title': 'Sales Performance Dashboard',
        'description': 'Built an interactive Power BI dashboard analyzing sales performance across multiple regions, resulting in 15% increase in quarterly revenue.',
        'technologies': ['Power BI', 'SQL Server', 'DAX'],
        'image': '/static/images/img_1.jpg',
        'github': 'https://github.com/yourusername/sales-dashboard',
        'demo': 'https://app.powerbi.com/view?r=...'
    },
    {
        'title': 'Customer Segmentation Analysis',
        'description': 'Performed RFM analysis using Python to segment customers, leading to targeted marketing campaigns with 25% higher conversion rates.',
        'technologies': ['Python', 'Pandas', 'Scikit-learn', 'Matplotlib'],
        'image': '/static/images/img_2.png',
        'github': 'https://github.com/yourusername/customer-segmentation',
        'demo': None
    },
    {    'title': 'Healthcare Data Insights',
        'description': 'Implemented advanced analytics to enhance patient care outcomes, resulting in a 25% reduction in readmission rates and improved resource allocation in hospital settings.',
        'technologies': ['Tableau', 'MySQL', 'Time Series Analysis'],
        'image': '/static/images/img_3.png',
        'github': 'https://github.com/yourusername/supply-chain',
        'demo': 'https://public.tableau.com/views/...'
    }
]

EXPERIENCE = [
    {
        'title': 'Jr. Machine Learning Engineer',
        'company': 'Blue Cascade Pakistan',
        'period': 'April 2025 - Present',
        'responsibilities': [
            'Built interactive dashboards in Power BI and Looker Studio to track KPIs and business performance',
            'Lead BI initiatives for executive reporting and strategic decision-making',
            ' Developed and optimized SQL queries for data extraction, transformation, and reporting',
            ' Applied Python and Machine Learning techniques for predictive analysis and data modeling',
            
        ]
    },
    {
        'title': 'Business Intelligence Analyst',
        'company': 'Ai NEURALZ',
        'period': 'May 2024 - October 2024',
        'responsibilities': [
            'Analyzed web traffic using Looker studio, improving content strategy on HDHub4u online movies streaming platform.',
            'Performed ad-hoc analysis to support business decisions',
            'Developed interactive dashboards for sales and marketing teams',
            'Delivered data storytelling, stakeholder engagement, and presentations to support strategic decisions.'
        ]
    },
    {
        'title': 'Accenture North America Data Analytics and Visualization Job Simulation on Forage',
        'company': 'Forage',
        'period': 'June 2024 - July 2024',
        'responsibilities': [
             'Completed a simulation focused on advising a hypothetical social media client as a Data Analyst at Accenture',
             'Cleaned, modelled and analyzed 7 datasets to uncover insights into content trends to inform strategic decisions',
             'Prepared a PowerPoint deck and video presentation to communicate key insights for the client and internal stakeholders'
        ]
    }
]

CERTIFICATIONS = [
    {
        
        'credential_id': 'CDJXZEZG0NVD',
        'name': 'Business Intelligence ',
        'issuer': 'Google',
        'date': 'Aug 13, 2024',
        'description': 'Demonstrated expertise in preparing data, modeling data, visualizing data, analyzing data, and deploying and maintaining deliverables using Microsoft Power BI.',
        'skills': ['Power BI', 'DAX', 'Power Query', 'Data Modeling'],
        'image': '/static/images/img_4.png',
        'verify_url': 'https://www.coursera.org/account/accomplishments/professional-cert/CDJXZEZG0NVD'
    },
    
    {
        'name': 'Machine Learning with Python',
        'issuer': 'Freecodecamp',
        'date': 'July 2023',
        'credential_id': 'TS-2022-12345',
        'skills' : ['Data Preprocessing', 'Feature Engineering','Model Building & Evaluation', 'Hyperparmeter Tuning'],
        'description': 'I gained hands-on experience with algorithms and techniques such as supervised and unsupervised learning, neural networks, and data preprocessing',
        'image': '/static/images/img_5.png',
        'verify_url': 'https://www.freecodecamp.org/certification/AsadMujeeb/machine-learning-with-python-v7'
    },
    {
        'name': 'Data Analyst Track',
        'issuer': 'Datacamp',
        'date': '2022',
        'credential_id': 'GA-IQ-2022-789',
        'description': 'Focusing on data analysis techniques, predictive modeling, and statistical methods. This training has equipped me with the skills to extract insights from large datasets, enabling data-driven decision-making and enhancing business strategies',
        'skills': ['Numpy', 'Pandas','Matplotlib','Seaborn'],
        'image': '/static/images/img_6.png',
        'verify_url': 'https://www.datacamp.com/completed/statement-of-accomplishment/track/89e4b7150c0fca83684be3b236c24b27181505fe'
    },
    {
        'name': 'SQL Track',
        'issuer': 'Codecademy',
        'date': 'July 2024',
        'credential_id': 'AWS-CCP-2021-456',
        'description': 'Proficient in SQL for data querying, database design, and optimization, with expertise in creating complex queries, managing relationships between tables, and implementing efficient indexing strategies',
        'skills': ['Data Query', 'Database Design', 'Data Manipulation', 'Aggregation and Joins'],
        'image': '/static/images/img_7.png',
        'verify_url': 'https://www.codecademy.com/profiles/Asad-Mujeeb/certificates/042a4e5884e3eb6ea1f2a12be6abb851'
    }
]

VOLUNTEER_WORK = [

    {
        'organization': 'The Youth Matrix',
        'role': 'Data Science Lead',
        'period': 'May 2025 - Present',
        'description': 'Delivered an online Data Analytics Fellowship Program, empowering students to become data-driven experts by providing comprehensive training in Power BI, Tableau, SQL, and Excel.',
        'achievements': [
            'Designed hands-on projects that allowed participants to apply their skills in real-world scenarios, enhancing their ability to analyze and visualize data effectively.',
            'Actively addressed student queries and provided personalized support, ensuring clarity and understanding of complex concepts.',
            'Implemented a robust performance tracking system to evaluate each students progress and assess their assigned tasks, offering constructive feedback to enhance their learning experience and foster continuous improvement.'
        ],
        'image': '/static/images/img_9.jpg'
    },
    {
        'organization': 'Microsoft Learn Student Ambassadors Program',
        'role': 'Data Analytics Lead',
        'period': 'August 2024 - April 2025',
        'description': 'Provide pro-bono data science services to nonprofit organizations, helping them leverage data to increase their social impact.',
        'achievements': [
            'Built predictive models for homeless shelter capacity planning',
            'Created dashboards for education nonprofit to track student outcomes',
            'Mentored junior volunteers in data analysis techniques'
        ],
        'image': '/static/images/img_8.jpeg'
    }
    
]

EDUCATION = [
    {
        'degree': 'Bachelor of Information Technology',
        'institution': 'Bahauddin Zakariya University BZU - Multan',
        'period': '2021 - 2025',
        'cgpa': '3.56 /4.0',
        'relevant_coursework': [
            'Data Analysis & Visualization',
            'Machine Learning',
            'Database Management Systems',
            'Python Programming',
            'Statistics',
            'Software Engineering',
            'Project Management',
            'Report Writing'
        ],
        'thesis': 'Whatsapp Chat Analyzer'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=PROJECTS)

@app.route('/about')
def about():
    return render_template('about.html', skills=SKILLS, education=EDUCATION)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)

@app.route('/experience')
def experience():
    return render_template('experience.html', experience=EXPERIENCE)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # In a real application, you would send an email or save to database
        # For now, we'll just flash a success message
        flash(f'Thank you {name}! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html', certifications=CERTIFICATIONS)

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html', volunteer_work=VOLUNTEER_WORK)

if __name__ == '__main__':
    app.run(debug=True)
