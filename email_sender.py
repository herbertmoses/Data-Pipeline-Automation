import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()

# CONFIG
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


def send_email(file_path):

    msg = EmailMessage()
    msg["Subject"] = "ETL Pipeline Completed ✅"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    msg.set_content(f"""
    Hello,

    Your ETL pipeline has successfully completed.

    Cleaned file is available at:
    {file_path}

    Regards,
    Data Pipeline Automation
    """)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)