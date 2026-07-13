from pydantic import BaseModel


class FeedbackCreate(BaseModel):
    rating: int
    comment: str