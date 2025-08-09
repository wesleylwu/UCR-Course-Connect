from fastapi import FastAPI
from typing import List
from sheets_service import load_courses_data
import threading
import time
from contextlib import asynccontextmanager

courses_data = []


def refresh_data_periodically(interval_minutes=5):
    global courses_data
    while True:
        courses_data = load_courses_data()
        time.sleep(interval_minutes * 60)


@asynccontextmanager
async def lifespan(app: FastAPI):
    global courses_data
    courses_data = load_courses_data()
    thread = threading.Thread(target=refresh_data_periodically, daemon=True)
    thread.start()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/courses")
def search_courses(search: str = "") -> List[dict]:
    search_lower = search.lower()
    return [course for course in courses_data if course["course_code"].lower().startswith(search_lower)]


@app.get("/courses/{course_code}")
def get_course_reviews(course_code: str):
    course_code_lower = course_code.lower()
    return [course for course in courses_data if course["course_code"].lower() == course_code_lower]
