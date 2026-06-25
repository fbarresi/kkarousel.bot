# kkarousel.bot

A Telegram bot built with [python-telegram-bot](https://python-telegram-bot.org/).

## Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux

# Install the package with dev dependencies
pip install -e ".[dev]"

# Copy and fill in your bot token
copy .env.example .env
```

## Run

```bash
kkarousel-bot
# or
python -m kkarousel_bot.main
```

## Docker

```bash
# Copy and fill in environment variables
cp .env.example .env

# Build the image
docker build -t kkarousel-bot .

# Run the container
docker run --env-file .env kkarousel-bot
```

## Test

```bash
pytest
```

## Lint

```bash
ruff check src tests
```
