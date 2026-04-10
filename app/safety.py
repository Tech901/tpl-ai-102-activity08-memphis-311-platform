"""
Content Safety and prompt injection defense for Memphis 311 AI Platform.

Implements a defense-in-depth approach:
  1. Fast regex-based injection pattern detection (no API call needed)
  2. Azure Content Safety API for harmful content analysis

AI-102 Domain 1.4 - Implement responsible AI
"""
import os
import re

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Known prompt injection patterns (pre-filled for student reference)
# ---------------------------------------------------------------------------
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"disregard\s+(your\s+)?(previous|safety|prior)",
    r"you\s+are\s+now",
    r"forget\s+(your|all)\s+instructions",
    r"new\s+instructions",
    r"override\s+(safety|system|previous)",
    r"pretend\s+(you\s+are|the|to\s+be)",
    r"developer\s+mode",
    r"reveal\s+(all\s+)?(api|secret|password|key)",
    r"SYSTEM:\s*",
    r"ignore\s+safety",
    r"output\s+(all\s+)?environment\s+variables",
    r"(?i)(?:DROP|DELETE|INSERT|UPDATE)\s+TABLE",  # SQL injection
    r"<script",  # XSS
]

# ---------------------------------------------------------------------------
# Lazy client initialization
# ---------------------------------------------------------------------------
_content_safety_client = None


def _get_content_safety_client():
    """Lazily initialize the Azure Content Safety client."""
    global _content_safety_client
    if _content_safety_client is None:
        # TODO: Uncomment and configure
        #   from azure.ai.contentsafety import ContentSafetyClient
        #   from azure.core.credentials import AzureKeyCredential
        #   _content_safety_client = ContentSafetyClient(
        #       endpoint=os.environ["AZURE_CONTENT_SAFETY_ENDPOINT"],
        #       credential=AzureKeyCredential(
        #           os.environ["AZURE_CONTENT_SAFETY_KEY"]
        #       ),
        #   )
        raise NotImplementedError("Configure the Content Safety client in Step 5")
    return _content_safety_client


# ---------------------------------------------------------------------------
# Step 5.1 - Prompt injection detection (regex-based, fast)
# ---------------------------------------------------------------------------
def check_injection(text: str) -> dict:
    """Check text for prompt injection patterns.

    Scans input against INJECTION_PATTERNS using case-insensitive regex.

    Args:
        text: User input to check.

    Returns:
        dict with keys:
          - detected (bool): True if any injection pattern matched
          - pattern_matched (str or None): The pattern that matched, or None
    """
    # TODO: Step 5.1 - Iterate over INJECTION_PATTERNS
    #   Use re.search(pattern, text, re.IGNORECASE) for each pattern
    #   If any match is found, return detected=True with the pattern
    #   If none match, return detected=False with pattern_matched=None
    raise NotImplementedError("Implement check_injection in Step 5")


# ---------------------------------------------------------------------------
# Step 5.2 - Azure Content Safety API check
# ---------------------------------------------------------------------------
def check_content_safety(text: str) -> dict:
    """Check text for harmful content using Azure Content Safety API.

    Analyzes text across four harm categories: Hate, SelfHarm, Sexual,
    Violence. Each category returns a severity score (0-6).

    Args:
        text: User input to check.

    Returns:
        dict with keys:
          - safe (bool): True if all category severities are below threshold
          - categories (dict): Severity scores for each category
    """
    # TODO: Step 5.2 - Call _get_content_safety_client().analyze_text()
    #   Build an AnalyzeTextOptions request with the input text
    #   Check each category result severity (threshold: severity >= 2 is unsafe)
    #   Return safe=True/False and the category severity dict
    raise NotImplementedError("Implement check_content_safety in Step 5")


# ---------------------------------------------------------------------------
# Step 5.3 - Combined safety check
# ---------------------------------------------------------------------------
def full_safety_check(text: str) -> dict:
    """Run full safety check: injection patterns first, then Content Safety API.

    Defense-in-depth: the fast regex check catches obvious injection
    attempts without an API call. The Content Safety API catches
    harmful content that regex patterns miss.

    Args:
        text: User input to check.

    Returns:
        dict with keys:
          - safe (bool): True only if both checks pass
          - blocked_reason (str or None): Why the input was blocked
          - injection_detected (bool): Whether injection patterns matched
          - content_safety (dict): Content Safety API results
    """
    # TODO: Step 5.3 - Run check_injection() first (fast, no API call)
    #   If injection detected, return safe=False immediately
    #   Then run check_content_safety() for harmful content
    #   Combine results into the return dict
    raise NotImplementedError("Implement full_safety_check in Step 5")
