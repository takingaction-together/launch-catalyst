import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

MODEL = "claude-3-5-sonnet-latest"
MAX_TOKENS = 4096

BASE_DIR = Path(__file__).parent
PROMPTS_DIR = BASE_DIR / "prompts"
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)
(DATA_DIR / "projects").mkdir(exist_ok=True)
