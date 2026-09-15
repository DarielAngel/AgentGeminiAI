import os
import requests

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def preguntar_gemini(texto):

    url = (
        "https://generativelanguage.googleapis.com/"
        f"v1beta/models/gemini-3.6-flash:generateContent?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": texto
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

    data = response.json()

    return (
        data["candidates"][0]
        ["content"]["parts"][0]["text"]
    )


async def responder(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    pregunta = update.message.text

    await update.message.reply_text(
        "Pensando..."
    )

    try:

        respuesta = preguntar_gemini(
            pregunta
        )

        await update.message.reply_text(
            respuesta[:4000]
        )

    except Exception as e:

        await update.message.reply_text(
            f"Error:\n{str(e)}"
        )


app = (
    ApplicationBuilder()
    .token(BOT_TOKEN)
    .build()
)

app.add_handler(
    MessageHandler(
        filters.TEXT,
        responder
    )
)

print("Bot iniciado")

app.run_polling()