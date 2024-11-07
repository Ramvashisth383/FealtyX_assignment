# app/ollama_integration.py

import requests
import json
from app.models import Student

def generate_student_summary(student: Student) -> str:
    url = "http://localhost:11434/api/generate"

    prompt = f"give me the summary of the student in a single paragraph don't use bold and higlight word  ellobarte the summary \nName: {student.name}\nAge: {student.age}\nEmail: {student.email}\n"

    data = {
        "model": "llama3.2",
        "prompt": prompt
    }

    try:
        with requests.post(url, json=data, stream=True) as response:
            if response.status_code == 200:
                final_response = ""
                for chunk in response.iter_lines(decode_unicode=True):
                    if chunk:
                        chunk_data = json.loads(chunk)
                        final_response += chunk_data.get("response", "")
                        if chunk_data.get("done", False):
                            break
                return final_response
            else:
                return response.status_code
    except requests.exceptions.RequestException as e:
        return e
    except json.JSONDecodeError as e:
        return e
