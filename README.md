# 🤖 AgentGeminiAI — AI assistant on Telegram

A Telegram bot that answers any text message using **Google Gemini**, deployed to the cloud on **Railway**. The repository also includes small scripts to compare LLM providers (Gemini, Cerebras, OpenRouter) by answer quality, latency and cost before choosing one.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-22-26A5E4?logo=telegram&logoColor=white)
![Gemini](https://img.shields.io/badge/Google-Gemini_API-8E75B2?logo=googlegemini&logoColor=white)
![Railway](https://img.shields.io/badge/deploy-Railway-0B0D0E?logo=railway&logoColor=white)

## How it works

```
Telegram user ──► python-telegram-bot (polling) ──► Gemini REST API ──► reply (≤ 4000 chars)
```

1. The bot receives a text message and immediately replies *"Pensando…"* so the user knows it is working.
2. It sends the question to the Gemini `generateContent` endpoint.
3. It returns the answer, trimmed to Telegram's message limit; any error is reported back to the chat instead of failing silently.

## Files

| File | Purpose |
|---|---|
| `bot.py` | The bot itself |
| `listar_modelos_gemini.py` | Lists the Gemini models available for your API key |
| `test_gemini.py`, `test_rest_gemini.py` | Gemini via SDK and via raw REST |
| `test_cerebras.py`, `test_openrouter.py`, `test_ai.py` | Same prompt against other providers, for comparison |
| `Procfile`, `railway.json`, `runtime.txt` | Cloud deployment (Railway / Heroku-style) |

## Run it locally

```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file (it is git-ignored):

```env
BOT_TOKEN=your-telegram-bot-token        # from @BotFather
GEMINI_API_KEY=your-gemini-api-key       # from Google AI Studio
# optional, only for the comparison scripts
CEREBRAS_API_KEY=
OPENROUTER_API_KEY=
```

```bash
python bot.py
```

## Deploy on Railway

1. Create a new project from this repository.
2. Add `BOT_TOKEN` and `GEMINI_API_KEY` as environment variables.
3. Railway runs `python bot.py` (see `railway.json`).

## Ideas for next steps

- Conversation memory per chat and a system prompt for a specific business (FAQ bot).
- `/start` and `/help` commands, rate limiting and usage logging.
- Answer from the business's own data (RAG) or trigger workflows through **n8n**.

---

Made by **[Dariel Angel Arro Moreno](https://darielangel.github.io)** · I build AI bots and automations for businesses — [let's talk](mailto:darielarrom@gmail.com).
