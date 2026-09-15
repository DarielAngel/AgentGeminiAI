from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("CEREBRAS_API_KEY"),
    base_url="https://api.cerebras.ai/v1"
)

response = client.chat.completions.create(
    model="qwen-3.8-27b",
    messages=[
        {
            "role": "user",
            "content": "Responde solamente: FUNCIONA"
        }
    ]
)

print(response.choices[0].message.content)