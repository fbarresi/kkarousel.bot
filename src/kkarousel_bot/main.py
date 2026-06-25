"""Entry point for kkarousel.bot."""

import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from kkarousel_bot.config import get_allowed_usernames, get_token
from kkarousel_bot.handlers import echo, help_command, photo, start

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def build_user_filter() -> filters.BaseFilter:
    usernames = get_allowed_usernames()
    logger.info("Allowed usernames: %s", usernames)
    return filters.User(username=list(usernames))


def main() -> None:
    app = ApplicationBuilder().token(get_token()).build()

    allowed = build_user_filter()

    app.add_handler(CommandHandler("start", start, filters=allowed))
    app.add_handler(CommandHandler("help", help_command, filters=allowed))
    app.add_handler(MessageHandler(allowed & filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(MessageHandler(allowed & filters.PHOTO, photo))

    logger.info("Bot started. Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
