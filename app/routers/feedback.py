from app.services.email import send_feedback_email
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/feedback")
async def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db)
):

    new_feedback = Feedback(
        rating=feedback.rating,
        comment=feedback.comment
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    print("Feedback saved to database")

    try:
        print("Sending email...")

        await send_feedback_email(
            feedback.rating,
            feedback.comment
        )

        print("Email sent successfully")

    except Exception as e:
        print("EMAIL ERROR:", e)

    return {
        "message": "Feedback saved",
        "id": new_feedback.id
    }