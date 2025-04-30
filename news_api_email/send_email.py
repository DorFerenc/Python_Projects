import smtplib, ssl
import os
from dotenv import load_dotenv
from email.message import EmailMessage

def send_email(subject, body, to_email):
    """
    Function to send an email using Brevo SMTP (TLS connection) with UTF-8 support.

    Environment Variables Required:
    - SMTP_SERVER
    - SMTP_PORT
    - SENDER_EMAIL
    - EMAIL_PASSWORD

    Parameters:
    - subject: Subject of the email.
    - body: Body content of the email (should be bytes).
    - to_email: Recipient's email address.

    Returns:
    - None
    """

    load_dotenv()

    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    print(f"Trying to connect to {smtp_server}:{smtp_port}...")
    print(f"Sender email: {sender_email}")
    print(f"Recipient email: {to_email}")

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            print("✅ Connection successful and login worked!")

            # Compose message with UTF-8 support
            msg = EmailMessage()
            msg.set_content(body.decode('utf-8'))
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = to_email

            server.send_message(msg)
            print("✅ Email sent successfully!")

    except Exception as e:
        print(f"❌ Error occurred: {e}")

