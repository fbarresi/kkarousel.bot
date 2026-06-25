"""Tests for the photo handler."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from kkarousel_bot.handlers import photo


def _make_photo_update(file_id: str = "abc123") -> MagicMock:
    tg_file = AsyncMock()
    tg_file.file_id = file_id
    tg_file.download_as_bytearray = AsyncMock(return_value=bytearray(b"fake-image-data"))

    photo_size = AsyncMock()
    photo_size.get_file = AsyncMock(return_value=tg_file)

    update = MagicMock()
    update.message.photo = [photo_size]  # single size for simplicity
    update.message.reply_text = AsyncMock()
    return update


@pytest.mark.asyncio
async def test_photo_upload_success():
    update = _make_photo_update()
    with patch("kkarousel_bot.handlers.upload_image", new=AsyncMock(return_value={"status": "ok"})) as mock_upload, \
         patch("kkarousel_bot.handlers.get_api_url", return_value="https://example.com"), \
         patch("kkarousel_bot.handlers.get_api_key", return_value="test-key"):
        await photo(update, MagicMock())

    mock_upload.assert_called_once_with(
        b"fake-image-data", "abc123.jpg", "https://example.com", "test-key"
    )
    update.message.reply_text.assert_called_once()
    assert "✅" in update.message.reply_text.call_args[0][0]


@pytest.mark.asyncio
async def test_photo_upload_failure_replies_with_error():
    update = _make_photo_update()
    with patch("kkarousel_bot.handlers.upload_image", new=AsyncMock(side_effect=Exception("network error"))), \
         patch("kkarousel_bot.handlers.get_api_url", return_value="https://example.com"), \
         patch("kkarousel_bot.handlers.get_api_key", return_value="test-key"):
        await photo(update, MagicMock())

    update.message.reply_text.assert_called_once()
    assert "❌" in update.message.reply_text.call_args[0][0]
