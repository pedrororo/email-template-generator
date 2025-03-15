# Email Template Generator with PDF Export 📧📄

Python tool to generate personalized email templates and export them to text files and modern PDFs.

---

## Features :sparkles:

- **Dynamic Email Generation**  
  Replace placeholders in templates with values from `config.ini`.
- **Multiple Templates**  
  Choose between formal, casual, or default templates via CLI or config.
- **Stylish PDF Export**  
  Modern design with clean typography and professional layout.
- **Modular Architecture**  
  Separated into reusable components for easy maintenance.
- **Comment Support**  
  Use `#` to disable fields (e.g., portfolio links).

---

## Installation :wrench:

### Prerequisites
- Python 3.7+
- pip

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/email-template-generator.git
cd email-template-generator

# Install dependencies
pip install -r requirements.txt

# Create required directories
mkdir template email_application
```



### Project Structure :file_folder:

```bash
email-template-generator/
├── main.py                  # Application entry point
├── email_generator/         # Core functionality modules
│   ├── config_handler.py    # Configuration parsing
│   ├── template_engine.py   # Template processing
│   └── utils.py             # Helper functions
├── template/                # Email templates
│   ├── template_default.txt
│   ├── template_formal.txt
│   └── template_casual.txt
├── email_application/       # Output directory
├── config.ini               # Configuration file
└── README.md
```


### Configuration :gear:

The config.ini file contains all the necessary details for generating the email.

Example config.ini

```bash
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
portfolio_link = # (commented out)
linkedin_link = https://linkedin.com/in/johndoe
contact_info = johndoe@example.com | +1234567890
email_greeting = Dear {hiring_manager},
email_closing = Best regards,
template_choice = formal
```

### Notes:

-  Use '#' to comment out fields (e.g., portfolio_link = #).

-   Ensure all required fields are filled in the [ApplicationDetails] section.


### Usage :rocket:

#### Generate email

```bash
# Use specific template
python3 main.py formal
python3 main.py casual

# Use default template from config.ini
python3 main.py
```

### Output Files

Example Output:

```bash
email_application/
├── subject.txt
├── email_body.txt
└── application_letter.pdf
```

### Contributing :handshake:


1. Fork the repository
2. Create your feature branch:

```bash
git checkout -b feature-name
```
3. Commit changes
```bash
git commit -m "Add feature or fix"```
```
4. Push to branch
```bash
git push origin feature-name
```
5. Open a pull request


### License :page_with_curl:

This project uses the [MIT License](https://opensource.org/licenses/MIT).  
See [LICENSE](LICENSE) for the full text.


### Acknowledgments :pray:

Built with ReportLab for PDF generation

Inspired by modern resume/CV templates
