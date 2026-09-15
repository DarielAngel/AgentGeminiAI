import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

url = (
    "https://generativelanguage.googleapis.com/"
    f"v1beta/models/gemini-3.6-flash:generateContent?key={API_KEY}"
)

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Responde solamente FUNCIONA"
                }
            ]
        }
    ]
}

response = requests.post(
    url,
    json=payload,
    timeout=60
)

print(response.status_code)
print(response.text)