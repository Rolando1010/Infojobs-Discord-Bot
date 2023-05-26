import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
INFOJOBS_TOKEN = os.getenv("INFOJOBS_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

BASE_DIRECTORY = Path(__file__).resolve().parent.parent
STATISTICS_CHARTS_DIRECTORY = os.path.join(BASE_DIRECTORY, "src/jobs/statistics/charts")