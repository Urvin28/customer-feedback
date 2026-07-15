import os
import resend
from dotenv import load_dotenv

load_dotenv()


resend.api_key = os.getenv("RESEND_API_KEY")


def send_feedback_email(
    rating: int,
    comment: str
):

    print("EMAIL FUNCTION STARTED")

    try:

        params = {
            "from": "onboarding@resend.dev",
            "to": [os.getenv("BUSINESS_EMAIL")],
            "subject": "New Customer Feedback",
            "html": f"""
            <h2>New Customer Feedback</h2>

            <p><strong>Rating:</strong> {rating}/5</p>

            <p><strong>Comment:</strong></p>

            <p>{comment}</p>
            """
        }

        email = resend.Emails.send(params)

        print("EMAIL SENT SUCCESSFULLY")
        print(email)


    except Exception as e:

        print("EMAIL ERROR:", repr(e))