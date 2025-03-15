import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


def ensure_directory_exists(directory):
    """Ensures that the specified directory exists. Creates it if it doesn't."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def export_to_files(subject, email_body, subject_file, body_file):
    """Exports the subject and email body to separate files."""
    # Write the subject to a file
    with open(subject_file, 'w', encoding='utf-8') as file:
        file.write(subject)
    
    # Write the email body to a file
    with open(body_file, 'w', encoding='utf-8') as file:
        file.write(email_body)


# In email_generator/utils.py

def export_to_pdf(subject, email_body, config, pdf_file):
    """Exports email content to a modern styled PDF"""
    doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=50, bottomMargin=40,
                            title=subject)  # Set the title to avoid (anonymous)
    
    styles = getSampleStyleSheet()
    style_normal = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14
    )
    
    heading_style = ParagraphStyle(
        'Heading1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=colors.HexColor('#2E4053'),
        spaceAfter=12
    )
    
    subheading_style = ParagraphStyle(
        'Subheading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=colors.HexColor('#34495E'),
        spaceAfter=6
    )
    
    link_style = ParagraphStyle(
        'LinkStyle',
        parent=styles['Normal'],
        textColor=colors.HexColor('#2980B9'),
        underline=True
    )

    story = []
    
    # Header Section
    header_text = Paragraph(subject, heading_style)
    story.append(header_text)
    
    # Horizontal line
    story.append(Spacer(1, 12))
    line = canvas.Canvas(pdf_file)
    line.setStrokeColor(colors.HexColor('#D5D8DC'))
    line.line(72, 750, 540, 750)
    story.append(Spacer(1, 18))
    
    # Body Content
    body_parts = email_body.split('\n\n')
    for part in body_parts:
        if part.startswith('Dear'):
            story.append(Paragraph(part, subheading_style))
            story.append(Spacer(1, 12))
        elif 'Relevant Experience' in part:
            story.append(Paragraph(part, subheading_style))
        elif 'Main Responsibility' in part:
            story.append(Paragraph(part, subheading_style))
        elif 'Relevant Areas' in part:
            story.append(Paragraph(part, subheading_style))
        elif 'Specific Tools' in part:
            story.append(Paragraph(part, subheading_style))
        elif 'Additional Resources' in part:
            story.append(Paragraph(part, subheading_style))
            # Process links
            resources = part.split('\n')[1:]
            for res in resources:
                if res.strip() and not res.startswith('#'):
                    story.append(Paragraph(res, link_style))
        else:
            story.append(Paragraph(part.replace('\n', '<br/>'), style_normal))
            story.append(Spacer(1, 12))
    
    # Footer with contact info
    contact_info = config.get('contact_info', 'N/A')
    github = config.get('github_link', '#').strip()
    linkedin = config.get('linkedin_link', '#').strip()
    portfolio = config.get('portfolio_link', '').strip()

    footer_data = [
        [Paragraph("Contact:", subheading_style), 
         Paragraph(contact_info, style_normal)],
        [Paragraph("GitHub", link_style), Paragraph(github, link_style) if github != '#' else ''],
        [Paragraph("LinkedIn", link_style), Paragraph(linkedin, link_style) if linkedin != '#' else '']
    ]
    
    # Only add Portfolio row if it's not a comment or empty
    if portfolio and not portfolio.startswith('#'):
        footer_data.append([Paragraph("Portfolio", link_style), Paragraph(portfolio, link_style)])
    
    footer_table = Table(footer_data, colWidths=[100, 300])
    footer_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#D5D8DC')),
    ]))
    
    story.append(Spacer(1, 24))
    story.append(footer_table)
    
    doc.build(story)