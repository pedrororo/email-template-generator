def read_template(template_file):
    """Reads the email template file and returns its content as a string."""
    with open(template_file, 'r', encoding='utf-8') as file:
        return file.read()

def generate_email(config, template):
    """Generates the email content by replacing placeholders in the template."""
    # Extract configuration values
    your_name = config['your_name']
    position_title = config['position_title']
    hiring_manager = config['hiring_manager']
    enterprise_name = config['enterprise_name']
    relevant_experience = config['relevant_experience']
    main_responsibility = config['main_responsibility']
    relevant_areas = config['relevant_areas']
    specific_tools = config['specific_tools']
    cv_attachment = config.getboolean('cv_attachment')
    github_link = config['github_link'].strip()  # Remove leading/trailing whitespace
    portfolio_link = config['portfolio_link'].strip()  # Remove leading/trailing whitespace
    linkedin_link = config['linkedin_link'].strip()  # Remove leading/trailing whitespace
    contact_info = config['contact_info']
    
    # Replace placeholders in email_greeting and email_closing
    email_greeting = config['email_greeting'].format(hiring_manager=hiring_manager)
    email_closing = config['email_closing']

    # Generate the subject
    subject = f"{your_name} – Application for {position_title} at {enterprise_name}"

    # Prepare additional resources
    additional_resources = ""
    if github_link and not github_link.startswith("#"):
        additional_resources += f"- GitHub: {github_link}\n"
    if portfolio_link and not portfolio_link.startswith("#"):
        additional_resources += f"- Portfolio: {portfolio_link}\n"
    if linkedin_link and not linkedin_link.startswith("#"):
        additional_resources += f"- LinkedIn: {linkedin_link}\n"

    # Replace placeholders in the template
    email_body = template.format(
        your_name=your_name,
        position_title=position_title,
        hiring_manager=hiring_manager,
        enterprise_name=enterprise_name,
        relevant_experience=relevant_experience,
        main_responsibility=main_responsibility,
        relevant_areas=relevant_areas,
        specific_tools=specific_tools,
        additional_resources=additional_resources.strip(),
        contact_info=contact_info,
        email_greeting=email_greeting,
        email_closing=email_closing
    )

    return subject, email_body