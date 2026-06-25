"""Tests for bot handlers."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from kkarousel_bot.handlers import echo, help_command, start


def _make_update(text: str) -> MagicMock:
    update = MagicMock()
    update.message.text = text
    update.message.reply_text = AsyncMock()
    return update


@pytest.mark.asyncio
async def test_start_replies():
    update = _make_update("/start")
    await start(update, MagicMock())
    update.message.reply_text.assert_called_once()


@pytest.mark.asyncio
async def test_help_replies():
    update = _make_update("/help")
    await help_command(update, MagicMock())
    update.message.reply_text.assert_called_once()


@pytest.mark.asyncio
async def test_echo_replies_with_same_text():
    update = _make_update("hello world")
    await echo(update, MagicMock())
    update.message.reply_text.assert_called_once_with("hello world")
