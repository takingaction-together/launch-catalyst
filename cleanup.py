import asyncio
from telegram import Bot
from config import TELEGRAM_BOT_TOKEN

async def reset():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    print("Force-closing any existing Telegram connections...")
    # This deletes the webhook AND drops all 'hanging' updates causing the conflict
    await bot.delete_webhook(drop_pending_updates=True)
    print("Success! The path is clear.")

if __name__ == "__main__":
    asyncio.run(reset())