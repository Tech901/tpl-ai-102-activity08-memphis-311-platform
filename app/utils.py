"""
Shared utility helpers for Memphis 311 AI Platform.
"""
import base64
import json
import os


def load_json(path: str):
    """Load and parse a JSON file.

    Args:
        path: Path to the JSON file.

    Returns:
        Parsed JSON content (dict or list).
    """
    with open(path) as f:
        return json.load(f)


def write_json(path: str, data) -> None:
    """Write data to a JSON file with pretty formatting.

    Args:
        path: Destination file path.
        data: JSON-serializable data.
    """
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def encode_image_base64(image_path: str) -> str:
    """Read an image file and return its base64-encoded string.

    Args:
        image_path: Path to the image file.

    Returns:
        Base64-encoded string of the image bytes.
    """
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
