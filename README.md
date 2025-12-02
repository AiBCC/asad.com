# Business Intelligence Portfolio - Flask Application

This is a professional portfolio website built with Flask, specifically designed for Business Intelligence professionals.

## Project Structure

\`\`\`
bi-portfolio-flask/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # Jinja2 templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── about.html        # About page
│   ├── projects.html     # Projects showcase
│   ├── experience.html   # Professional experience
│   ├── contact.html      # Contact form
│   └── blog.html         # Blog page
└── static/              # Static files
    ├── css/
    │   └── style.css    # Custom CSS styles
    ├── js/
    │   └── main.js      # JavaScript functionality
    └── images/          # Portfolio images (create this folder)
\`\`\`

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: Bootstrap 5 (CSS framework)
- **Icons**: Font Awesome
- **Styling**: Custom CSS with Bootstrap
- **JavaScript**: Vanilla JS for interactions

## Installation & Setup

1. Install Python dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. Run the application:
   \`\`\`bash
   python app.py
   \`\`\`

3. Open your browser and navigate to `http://localhost:5000`

## Features

- Responsive design optimized for all devices
- Professional BI-focused content and styling
- Interactive contact form
- Project showcase with technology tags
- Professional experience timeline
- Blog section for thought leadership
- Smooth animations and hover effects

## Customization

1. **Personal Information**: Update the personal details in `app.py` and templates
2. **Projects**: Modify the `PROJECTS` list in `app.py` to showcase your work
3. **Experience**: Update the `EXPERIENCE` list with your professional background
4. **Skills**: Customize the `SKILLS` dictionary with your technical and business skills
5. **Styling**: Modify `static/css/style.css` for custom styling
6. **Images**: Add your portfolio images to the `static/images/` directory

## Deployment

This Flask application can be deployed to various platforms:
- Heroku
- Vercel
- PythonAnywhere
- DigitalOcean App Platform
- AWS Elastic Beanstalk

## Note

This project uses Bootstrap 5 for styling, not Tailwind CSS. All styling is handled through Bootstrap classes and custom CSS in the `style.css` file.
