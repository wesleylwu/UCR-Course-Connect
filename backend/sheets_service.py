import os
import re
import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]

script_dir = os.path.dirname(os.path.abspath(__file__))
creds_path = os.path.join(script_dir, "credentials.json")

creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1DxyA0D6VEFQbkEmYk4hlNDshHdmctjGEn1D-6-kFocM"
sheet = client.open_by_key(sheet_id).sheet1


def load_courses_data():
    rows = sheet.get_all_values()
    data_rows = rows[1:]

    courses = []
    current_course = None

    for row in data_rows:
        if not row or not row[0]:
            if current_course:
                review_entry = {
                    "course_code": current_course["course_code"],
                    "difficulty": None,
                    "review": row[1] if len(row) > 1 else None,
                    "date": row[2] if len(row) > 2 else None,
                }
                courses.append(review_entry)
            continue

        course_code = row[0].strip()
        if re.match(r"^[a-zA-Z]{2,4}\d+[a-zA-Z]?$", course_code):
            current_course = {
                "course_code": course_code,
                "difficulty": row[1] if len(row) > 1 else None,
                "review": row[2] if len(row) > 2 else None,
                "date": row[3] if len(row) > 3 else None,
            }
            courses.append(current_course)


    return courses
