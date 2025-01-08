"""
Author: Golemon
Created: 2025.1.8
Version: 1.0

Description:
This script defines a set of functions to send email messages via SMTP, using settings from a configuration file (.ini). 
It includes a `read_config` function to load the necessary settings (such as SMTP server, port, sender, recipient, etc.) 
and a `send_email` function to handle the process of connecting to the SMTP server and sending the email. 
The email sending process is customizable via the configuration file, making the script flexible for different use cases.

The configuration file must include the following keys under the `[EMAIL]` section:
    - smtp_server: SMTP server address (e.g., 'smtp.gmail.com')
    - port: Port number for the SMTP connection (usually 587 for TLS)
    - sender: The sender email address
    - recipient: The recipient email address
    - app_password: Application-specific password for the sender account
    - subject: The subject of the email
    - content: The content/body of the email
    - timeout: Timeout value for the connection in seconds
"""
import smtplib
from email.message import EmailMessage
import configparser

def read_config(file_path):
    """
    Read email settings from the .ini configuration file.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        dict: Email settings from the configuration file.
    """
    config = configparser.ConfigParser()

    # Explicitly specify encoding as utf-8
    with open(file_path, 'r', encoding='utf-8') as file:
        config.read_file(file)
    return {
        'smtp_server': config['EMAIL']['smtp_server'],
        'port': int(config['EMAIL']['port']),
        'sender': config['EMAIL']['sender'].strip('"'),
        'recipient': config['EMAIL']['recipient'].strip('"'),
        'app_password': config['EMAIL']['app_password'].strip('"'),
        'subject': config['EMAIL']['subject'].strip('"'),
        'content': config['EMAIL']['content'].strip('"'),
        'timeout': int(config['EMAIL']['timeout'])
    }

def send_email(config):
    """
    Send an email based on the configuration.

    Args:
        config (dict): Email settings read from the configuration file.
    
    Returns:
        str: Message indicating whether the email was sent successfully or failed.
    """
    # Create the email object
    msg = EmailMessage()
    msg['Subject'] = config['subject']
    msg['From'] = config['sender']
    msg['To'] = config['recipient']
    msg.set_content(config['content'])

    try:
        # Connect to SMTP server and send the email
        with smtplib.SMTP(config['smtp_server'], config['port'], timeout=config['timeout']) as server:
            server.set_debuglevel(1)  # Enable debug mode to output detailed information
            server.starttls()  # Enable TLS encryption
            server.login(config['sender'], config['app_password'])  # Log in to the email account
            server.send_message(msg)  # Send the email
        return "Email sent successfully!"
    except Exception as e:
        return f"Email sending failed: {e}"

def start():
    config = read_config('send_email.ini')
    result = send_email(config)
    print(result)

# Read configuration and send the email
if __name__ == "__main__":
    # Read the configuration file
    config = read_config('send_email.ini')
    
    # Call the function to send the email
    result = send_email(config)
    print(result)
