from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv()


conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=465,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
)


def send_feedback_email(
    rating: int,
    comment: str
):

    print("EMAIL FUNCTION STARTED")

    message = MessageSchema(
        subject="New Customer Feedback",
        recipients=[os.getenv("BUSINESS_EMAIL")],
        body=f"""
New Feedback Received:

Rating: {rating}/5

Comment:
{comment}
""",
        subtype="plain"
    )

    fm = FastMail(conf)

    try:
        print("CONNECTING TO EMAIL SERVER")

        import asyncio
        asyncio.run(fm.send_message(message))

        print("EMAIL SENT SUCCESSFULLY")

    except Exception as e:
        print("EMAIL ERROR:", repr(e))