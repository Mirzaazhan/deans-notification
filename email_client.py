import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
import pprint


#Get API keys using env
user = os.environ.get('GMAIL_USER')
password = os.environ.get('GMAIL_PASSWORD')
# from configparser import ConfigParser
# config = ConfigParser()
# config.read('config.ini')
# user = config.get('gmail', 'user')
# password = config.get('gmail', 'password')


# -------------------------------------------------------------
# Helper to Format Crisis Sections Using Templates
# -------------------------------------------------------------
def generate_section(crisis_list):
    """Generate formatted lines from a list of crisis dictionaries."""
    if not crisis_list:
        return "No items reported.\n"

    lines = []
    for crisis in crisis_list:
        lines.append(
            f"Report Time: {crisis.get('crisis_time', 'N/A')}\n"
            f"Location: {crisis.get('location', 'N/A')}\n"
            f"Location2: {crisis.get('location2', 'N/A')}\n"
            f"Crisis Type: {crisis.get('type', 'N/A')}\n"
            f"Assistance Requested: {crisis.get('crisis_assistance', 'N/A')}\n"
            f"Description: {crisis.get('crisis_description', 'N/A')}\n"
        )
    return "\n".join(lines)


# -------------------------------------------------------------
# Build Email Body Using Template
# -------------------------------------------------------------
def build_email_body(data):
    """Load email template and inject formatted crisis sections."""
    try:
        with open("email_template.txt", "r") as file:
            template = file.read()
    except FileNotFoundError:
        logging.error("email_template.txt not found!")
        raise

    formatted_body = template.format(
        timestamp=datetime.now().strftime("%I:%M %p on %B %d, %Y"),
        new_crisis_section=generate_section(data.get('new_crisis', [])),
        resolved_crisis_section=generate_section(data.get('recent_resolved_crisis', [])),
        active_crisis_section=generate_section(data.get('active_crisis', [])),
    )

    return formatted_body


# -------------------------------------------------------------
# Main Email Sending Logic with Error Handling & Logging
# -------------------------------------------------------------
def main(emailadd, subject, data):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = emailadd
    msg['Subject'] = subject

    # Build email body from template
    body = build_email_body(data)
    msg.attach(MIMEText(body, 'plain'))
    message_string = msg.as_string()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        logging.info("Connecting to Gmail SMTP...")
        server.login(user, password)
        logging.info("SMTP login successful.")

        server.sendmail(user, emailadd, message_string)
        server.quit()

        logging.info("Email successfully sent to %s", emailadd)
        print("Email sent!")

    except smtplib.SMTPAuthenticationError:
        logging.error("SMTP authentication failed.")
    except smtplib.SMTPException as smtp_err:
        logging.error("SMTP error: %s", smtp_err)
    except Exception as e:
        logging.error("Unexpected error occurred: %s", e)
