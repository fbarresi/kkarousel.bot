"""Client for the kkarousel upload API."""

import logging

import httpx

logger = logging.getLogger(__name__)


async def upload_image(image_bytes: bytes, filename: str, api_url: str, api_key: str) -> dict:
    """Upload an image to POST /upload and return the parsed JSON response."""
    url = f"{api_url}/upload"
    headers = {"X-API-Key": api_key}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            headers=headers,
            files={"file": (filename, image_bytes, "application/octet-stream")},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
