import sys
import os
from email_generator.config_handler import read_config
from email_generator.template_engine import generate_email, read_template
from email_generator.utils import ensure_directory_exists, export_to_files, export_to_pdf


def main():
    # Define paths
    config_file = 'config.ini'
    template_dir = 'template'
    email_application_dir = 'email_application'
    
    # Ensure directories exist
    ensure_directory_exists(template_dir)
    ensure_directory_exists(email_application_dir)
    
    # Read the configuration
    config = read_config(config_file)
    
    # Determine which template to use - PRIORITY: CLI argument > config file
    template_choice = sys.argv[1].lower() if len(sys.argv) > 1 else config.get('template_choice', 'default').lower()
    
    # Map template_choice to the corresponding file
    template_map = {
        "formal": "template_formal.txt",
        "casual": "template_casual.txt",
        "default": "template_default.txt"
    }
    
    # Select the appropriate template file
    template_file_name = template_map.get(template_choice, "template_default.txt")
    template_file = os.path.join(template_dir, template_file_name)
    
    # Paths to the output files
    subject_file = os.path.join(email_application_dir, 'subject.txt')
    body_file = os.path.join(email_application_dir, 'email_body.txt')
    pdf_file = os.path.join(email_application_dir, 'application_letter.pdf')  # New PDF path

    
    # Read the selected template
    template = read_template(template_file)
    
    # Generate the email subject and body
    subject, email_body = generate_email(config, template)
    
    # Export the subject and email body to separate files
    export_to_files(subject, email_body, subject_file, body_file)
    export_to_pdf(subject, email_body, config, pdf_file)

    print(f"Subject has been exported to '{subject_file}'.")
    print(f"Email body has been exported to '{body_file}'.")
    print(f"PDF version created at '{pdf_file}'.")
if __name__ == "__main__":
    main()