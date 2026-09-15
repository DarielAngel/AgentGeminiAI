import requests

try:
    r = requests.get(
        "https://openrouter.ai/api/v1/models",
        timeout=20
    )

    print("STATUS:", r.status_code)

except Exception as e:
    print("ERROR:", e)