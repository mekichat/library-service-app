import os
from typing import cast
from pathlib import Path
from dotenv import load_dotenv

# app/config.py -> app -> book-api -> library-service-app
PROJECT_ROOT = Path(__file__).resolve().parents[2]

ENV_FILE = os.getenv("ENV_FILE", ".env")

env_path = PROJECT_ROOT / ENV_FILE

print("Loading env file:", env_path)

load_dotenv(env_path, override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

DATABASE_URL = cast(str, DATABASE_URL)