"""Tests for config helpers."""

import pytest

from kkarousel_bot.config import get_allowed_usernames


def test_parses_usernames(monkeypatch):
    monkeypatch.setenv("ALLOWED_USERNAMES", "alice,bob,charlie")
    assert get_allowed_usernames() == {"alice", "bob", "charlie"}


def test_strips_at_sign(monkeypatch):
    monkeypatch.setenv("ALLOWED_USERNAMES", "@alice,@bob")
    assert get_allowed_usernames() == {"alice", "bob"}


def test_lowercases_usernames(monkeypatch):
    monkeypatch.setenv("ALLOWED_USERNAMES", "Alice,BOB")
    assert get_allowed_usernames() == {"alice", "bob"}


def test_strips_whitespace(monkeypatch):
    monkeypatch.setenv("ALLOWED_USERNAMES", " alice , bob ")
    assert get_allowed_usernames() == {"alice", "bob"}


def test_raises_when_not_set(monkeypatch):
    monkeypatch.delenv("ALLOWED_USERNAMES", raising=False)
    with pytest.raises(RuntimeError, match="ALLOWED_USERNAMES"):
        get_allowed_usernames()
