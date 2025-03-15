# email-template-generator

Email Template Generator with PDF Export

This Python application generates personalized email templates based on configuration files and exports the content into text files and a modern-styled PDF document. The tool is modular, customizable, and designed to streamline the process of creating professional application letters or emails.


Table of Contents

- Features
- Installation
- Project Structure
- Configuration
- Usage
- Output
- Contributing
- License

Features
- Dynamic Email Generation: Replace placeholders in templates with values from a configuration file.
- Multiple Templates: Choose between formal, casual, or default email templates via command-line arguments or configuration.
- PDF Export: Generate a modern, styled PDF version of the email content.
- Modular Design: Code is organized into reusable modules for better maintainability.
- Customizable Styling: Modern design with clean typography, colors, and layout for the PDF output.

Installation
Prerequisites

Python 3.7 or higher
Pip (Python package manager)

Steps

Clone this repository:

git clone https://github.com/yourusername/email-template-generator.git
cd email-template-generator

Install the required dependencies:

pip install -r requirements.txt

Create the necessary directories:

mkdir template email_application

Add your configuration file (config.ini) and templates (template_formal.txt, template_casual.txt, etc.) to the respective

Project Structure

email-template-generator/
├── main.py                  # Entry point of the application
├── email_generator/         # Modularized code for email generation
│   ├── __init__.py          # Package initializer
│   ├── config_handler.py    # Handles configuration file reading
│   ├── template_engine.py   # Manages template processing
│   └── utils.py             # Utility functions (e.g., PDF export)
├── template/                # Directory for email templates
│   ├── template_default.txt
│   ├── template_formal.txt
│   └── template_casual.txt
├── email_application/       # Output directory for generated files
├── config.ini               # Configuration file
└── README.md                # This file

Configuration
The config.ini file contains all the necessary details for generating the email. Below is an example configuration:



[ApplicationDetails]
your_name = John Doe
position_title = Software Engineer
hiring_manager = Jane Smith
enterprise_name = TechCorp
relevant_experience = 5 years in software development
main_responsibility = Developing scalable web applications
relevant_areas = Backend development, API design
specific_tools = Python, Flask, Docker, AWS
cv_attachment = True
github_link = https://github.com/johndoe
portfolio_link = https://johndoe.com/portfolio
linkedin_link = https://linkedin.com/in/johndoe
contact_info = johndoe@example.com | +1234567890
email_greeting = Dear {hiring_manager},
email_closing = Best regards,
template_choice = formal


Notes:
Use # to comment out fields (e.g., portfolio_link = #).
Ensure all required fields are filled in the [ApplicationDetails] section.



Usage
Command-Line Arguments
You can specify the template type via command-line arguments:

python3 main.py formal
python3 main.py casual
python3 main.py default


If no argument is provided, the application will use the template_choice value from config.ini.

Example Commands
Generate a formal email:

python3 main.py formal

Generate a casual email:

python3 main.py casual

Use the default template:

python3 main.py



Output
The application generates the following files in the email_application/ directory:

subject.txt: Contains the email subject.
email_body.txt: Contains the full email body.
application_letter.pdf: A modern-styled PDF version of the email

Example Output:
email_application/
├── subject.txt
├── email_body.txt
└── application_letter.pdf


Contributing
We welcome contributions to improve this project! Here's how you can help:

Fork the repository.
Create a new branch for your feature or bug fix:

git checkout -b feature-name

Commit your changes:

git commit -m "Add feature or fix"

Push to your branch:

git push origin feature-name


Open a pull request on GitHub.
Please ensure your code adheres to PEP 8 standards and include tests if applicable.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Built using Python's reportlab library for PDF generation.
Inspired by modern resume/CV templates for the PDF styling.
Feel free to customize this README.md further to match your personal style or add additional sections like screenshots, FAQs, or future plans. Once you're satisfied, upload it to your GitHub repository alongside your code.
