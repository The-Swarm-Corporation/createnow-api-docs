import os
import requests
from typing import Optional, Dict, Any


def create_now_generate(
    prompt: str,
    media_type: Optional[str] = None,
    count: Optional[int] = 1,
    duration: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Generate AI content using the CreateNow API.

    Args:
        prompt (str): The prompt for content generation.
        media_type (Optional[str]): The type of media to generate ('image', 'music', 'video', 'speech'). Defaults to None.
        count (Optional[int]): The number of outputs to generate (1-4). Defaults to 1.
        duration (Optional[int]): Duration for music/speech in seconds. Defaults to None.

    Returns:
        Dict[str, Any]: The response from the API containing success status and generated content URLs.

    Raises:
        ValueError: If the prompt is empty or if count is out of range.
    """
    if not prompt:
        raise ValueError("Prompt cannot be empty.")
    if count < 1 or count > 4:
        raise ValueError("Count must be between 1 and 4.")

    api_key = os.getenv("CREATE_NOW_API_KEY")

    url = "https://createnow.xyz/api/v1/generate"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "prompt": prompt,
        "type": media_type,
        "count": count,
        "duration": duration,
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()
