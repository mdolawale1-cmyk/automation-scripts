"""Sends email notifications when system alerts are triggered."""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = "smtp.gmail.com"       # Replace with your SMTP server
SMTP_PORT = 587
SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_password"    # Use environment variables in production
RECIPIENT_EMAIL = "recipient@example.com"

def send_alert(subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECIPIENT_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()

        print("Alert email sent successfully ✅")
    except Exception as e:
        print(f"Failed to send alert email ❌ — {e}")

if __name__ == "__main__":
    # Example usage
    send_alert(
        subject="System Alert: High CPU Usage",
        body="CPU usage exceeded threshold. Immediate attention required."
    )
