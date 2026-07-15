from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv()



conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)


async def send_feedback_email(
    rating: int,
    comment: str
):

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
        await fm.send_message(message)
        print("Email sent successfully")
    except Exception as e:
        print("EMAIL ERROR:", repr(e))