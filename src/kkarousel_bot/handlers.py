"""Telegram bot command and message handlers."""

import logging

from telegram import Update
from telegram.ext import ContextTypes

from kkarousel_bot.api_client import upload_image
from kkarousel_bot.config import get_api_key, get_api_url

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    await update.message.reply_text("Hello! I'm kkarousel.bot. How can I help you?")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command."""
    await update.message.reply_text("Available commands:\n/start — Start the bot\n/help — Show this message")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo any text message back to the user."""
    await update.message.reply_text(update.message.text)


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Download the highest-resolution photo and forward it to the upload API."""
    # Telegram sends multiple sizes; pick the largest one
    photo_file = await update.message.photo[-1].get_file()
    image_bytes = await photo_file.download_as_bytearray()
    filename = f"{photo_file.file_id}.jpg"

    try:
        result = await upload_image(bytes(image_bytes), filename, get_api_url(), get_api_key())
        logger.info("Upload succeeded for %s: %s", filename, result)
        await update.message.reply_text("✅ Picture uploaded successfully!")
    except Exception as exc:
        logger.error("Upload failed for %s: %s", filename, exc)
        await update.message.reply_text("❌ Failed to upload the picture. Please try again later.")
