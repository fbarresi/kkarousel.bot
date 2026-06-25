"""Configuration loaded from environment variables."""

import os

from dotenv import load_dotenv

load_dotenv()


def get_token() -> str:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN environment variable is not set")
    return token


def get_allowed_usernames() -> set[str]:
    """Return the set of Telegram usernames allowed to interact with the bot.

    Set ALLOWED_USERNAMES as a comma-separated list of usernames (without @), e.g.:
        ALLOWED_USERNAMES=alice,bob,charlie
    """
    raw = os.getenv("ALLOWED_USERNAMES", "")
    if not raw.strip():
        raise RuntimeError("ALLOWED_USERNAMES environment variable is not set")
    return {u.strip().lstrip("@") for u in raw.split(",") if u.strip()}


def get_api_url() -> str:
    url = os.getenv("KKAROUSEL_API_URL")
    if not url:
        raise RuntimeError("KKAROUSEL_API_URL environment variable is not set")
    return url.rstrip("/")


def get_api_key() -> str:
    key = os.getenv("KKAROUSEL_API_KEY")
    if not key:
        raise RuntimeError("KKAROUSEL_API_KEY environment variable is not set")
    return key
