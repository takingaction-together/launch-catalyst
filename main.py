"""
Webhook server for production/deployment.
For local development, use run_polling.py instead.
"""
import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from telegram import Update

from bot import build_application
from config import TELEGRAM_BOT_TOKEN, WEBHOOK_URL

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)

ptb_app = build_application()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await ptb_app.initialize()
    webhook_url = f"{WEBHOOK_URL}/webhook"
    await ptb_app.bot.set_webhook(url=webhook_url)
    logging.getLogger(__name__).info("Webhook set to %s", webhook_url)
    await ptb_app.start()
    yield
    await ptb_app.stop()


app = FastAPI(lifespan=lifespan)


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, ptb_app.bot)
    await ptb_app.process_update(update)
    return {"ok": True}


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
