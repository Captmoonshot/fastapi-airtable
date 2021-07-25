from dotenv import load_dotenv
from functools import lru_cache
import os
import pathlib
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent   # src

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@lru_cache
def cached_dotenv():
    load_dotenv()

cached_dotenv()
# print('AIRTABLE_BASE_ID', os.getenv('AIRTABLE_BASE_ID', 'you-will-never-know'))

@app.get("/")
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.post("/")
def home_signup_view(request: Request, email: str = Form(...)):
    """
    TODO add CSRF for security
    """

    # to send email to airtable


    return templates.TemplateResponse("home.html", {
        "request": request,
        "submitted_email": email
    })









