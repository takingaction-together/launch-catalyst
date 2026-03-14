"""
Local development runner — uses polling instead of webhooks.
No ngrok or deployment needed. Just run: python run_polling.py
"""
import asyncio
import logging

from bot import build_application

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)


async def main():
    app = build_application()
    print("Bot running in polling mode. Send a message in Telegram to test.")
    async with app:
        await app.initialize()
        await app.start()
        await app.updater.start_polling(drop_pending_updates=True)
        await asyncio.Event().wait()  # run until interrupted


if __name__ == "__main__":
    asyncio.run(main())
