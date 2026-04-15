"""
Vision pipeline for Memphis 311 inspection photo intake.
Reuses patterns from Activity 4 (Inspector Vision).

Processes inspection photos through:
  1. Photo classification (category + confidence)
  2. Finding description (severity assessment)
"""
import os

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Lazy client initialization
# ---------------------------------------------------------------------------
_openai_client = None


def _get_openai_client():
    """Lazily initialize the Azure OpenAI client for vision tasks."""
    global _openai_client
    if _openai_client is None:
        # TODO: Uncomment and configure
        #   from openai import AzureOpenAI
        #   _openai_client = AzureOpenAI(
        #       azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        #       api_key=os.environ["AZURE_OPENAI_API_KEY"],
        #       api_version="2024-10-21",
        #   )
        raise NotImplementedError(
            "Configure the Azure OpenAI client in Step 2"
        )
    return _openai_client


# ---------------------------------------------------------------------------
# Step 2.1 - Photo Classification
# ---------------------------------------------------------------------------
def classify_photo(image_path: str) -> dict:
    """Classify an inspection photo into a city issue category.

    Sends the image to GPT-4o as a base64-encoded attachment and asks
    it to classify the issue type (e.g., Pothole, Graffiti, Streetlight,
    Trash/Litter, Sidewalk Damage, Other).

    Args:
        image_path: Path to the inspection photo file.

    Returns:
        dict with keys:
          - category (str): Issue category label
          - confidence (float): Classification confidence (0.0-1.0)
          - tags (list): Descriptive tags for the photo content
    """
    # TODO: Step 2.1 - Encode the image using utils.encode_image_base64()
    #   Build a chat message with image_url content type
    #   Call _get_openai_client().chat.completions.create()
    #   Parse the response to extract category, confidence, and tags
    raise NotImplementedError("Implement classify_photo in Step 2")


# ---------------------------------------------------------------------------
# Step 2.2 - Finding Description
# ---------------------------------------------------------------------------
def describe_finding(image_path: str) -> dict:
    """Generate a description and severity assessment for an inspection photo.

    Sends the image to GPT-4o and asks for a human-readable description
    of the finding along with a severity rating.

    Args:
        image_path: Path to the inspection photo file.

    Returns:
        dict with keys:
          - description (str): Human-readable finding description
          - severity (str): One of "low", "medium", "high", "critical"
    """
    # TODO: Step 2.2 - Encode the image using utils.encode_image_base64()
    #   Build a chat message asking for description and severity
    #   Call _get_openai_client().chat.completions.create()
    #   Parse the response to extract description and severity
    raise NotImplementedError("Implement describe_finding in Step 2")


# ---------------------------------------------------------------------------
# Step 2.3 - Full photo processing pipeline
# ---------------------------------------------------------------------------
def process_photo(image_path: str) -> dict:
    """Run the full vision pipeline on an inspection photo.

    Pipeline:
      1. Classify the photo into a category
      2. Generate a description and severity assessment

    Args:
        image_path: Path to the inspection photo file.

    Returns:
        dict with keys:
          - category (str)
          - confidence (float)
          - tags (list)
          - description (str)
          - severity (str)
    """
    # TODO: Step 2.3 - Chain classify_photo() and describe_finding()
    #   Merge both results into a single dict
    raise NotImplementedError("Implement process_photo in Step 2")
