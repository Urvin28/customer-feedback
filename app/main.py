from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

from app.database.database import engine, Base
from app.models.feedback import Feedback
from app.routers import feedback


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(feedback.router)


@app.get("/")
def home():
    return {"message": "Customer Feedback API is running"}


@app.get("/feedback-page", response_class=HTMLResponse)
def feedback_page():
    file_path = Path("app/templates/feedback.html")
    return file_path.read_text(encoding="utf-8")

@app.get("/customer-feedback", response_class=HTMLResponse)
def customer_feedback():
    file_path = Path("app/templates/customer_feedback.html")
    return file_path.read_text(encoding="utf-8")