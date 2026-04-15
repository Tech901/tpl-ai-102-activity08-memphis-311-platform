"""
NLP pipeline for Memphis 311 text complaint intake.
Reuses patterns from Activity 5 (Constituent Services Hub).

Processes text complaints through:
  1. PII redaction (must happen FIRST)
  2. Sentiment analysis
  3. Intent classification
  4. Key phrase extraction
"""
import os

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Lazy client initialization
# ---------------------------------------------------------------------------
_language_client = None
_openai_client = None


def _get_language_client():
    """Lazily initialize the Azure AI Language client."""
    global _language_client
    if _language_client is None:
        # TODO: Uncomment and configure
        #   from azure.ai.textanalytics import TextAnalyticsClient
        #   from azure.core.credentials import AzureKeyCredential
        #   _language_client = TextAnalyticsClient(
        #       endpoint=os.environ["AZURE_AI_LANGUAGE_ENDPOINT"],
        #       credential=AzureKeyCredential(
        #           os.environ["AZURE_AI_LANGUAGE_KEY"]
        #       ),
        #   )
        raise NotImplementedError(
            "Configure the AI Language client in Step 1"
        )
    return _language_client


def _get_openai_client():
    """Lazily initialize the Azure OpenAI client."""
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
            "Configure the Azure OpenAI client in Step 1"
        )
    return _openai_client


# ---------------------------------------------------------------------------
# Step 1.1 - PII Redaction
# ---------------------------------------------------------------------------
def redact_pii(text: str) -> dict:
    """Detect and redact PII from complaint text.

    Uses Azure AI Language PII detection to find personal information
    (names, SSNs, addresses, phone numbers) and replace them with
    category labels like [PERSON], [SSN], [ADDRESS].

    Args:
        text: Raw complaint text that may contain PII.

    Returns:
        dict with keys:
          - redacted_text (str): Text with PII replaced by labels
          - entities_found (list): List of entity category strings
          - entity_count (int): Number of PII entities detected
    """
    # TODO: Step 1.1 - Call _get_language_client().recognize_pii_entities()
    #   Pass the text as a single-element list
    #   Extract the redacted_text from the response
    #   Collect entity categories into a list
    #   Return the result dict
    raise NotImplementedError("Implement redact_pii in Step 1")


# ---------------------------------------------------------------------------
# Step 1.2 - Sentiment Analysis
# ---------------------------------------------------------------------------
def analyze_sentiment(text: str) -> dict:
    """Analyze sentiment of complaint text.

    Uses Azure AI Language to determine overall sentiment
    (positive, neutral, negative, mixed) with confidence scores.

    Args:
        text: Complaint text (should be redacted first).

    Returns:
        dict with keys:
          - sentiment (str): Overall sentiment label
          - confidence_scores (dict): Scores for positive, neutral, negative
          - key_phrases (list): Extracted key phrases
    """
    # TODO: Step 1.2 - Call _get_language_client().analyze_sentiment()
    #   Also call extract_key_phrases() for key phrases
    #   Combine sentiment label, confidence scores, and key phrases
    raise NotImplementedError("Implement analyze_sentiment in Step 1")


# ---------------------------------------------------------------------------
# Step 1.3 - Intent Classification
# ---------------------------------------------------------------------------
def classify_intent(text: str) -> str:
    """Classify the citizen's intent from complaint text.

    Uses Azure OpenAI to classify text into one of three intents:
      - "report-issue": Reporting a new problem
      - "check-status": Asking about an existing report
      - "ask-question": General question about services

    Args:
        text: Complaint text (should be redacted first).

    Returns:
        str: One of "report-issue", "check-status", "ask-question"
    """
    # TODO: Step 1.3 - Call _get_openai_client().chat.completions.create()
    #   Use a system prompt that instructs classification into 3 intents
    #   Parse the response to extract one of the three intent labels
    #   Default to "report-issue" if classification is ambiguous
    raise NotImplementedError("Implement classify_intent in Step 1")


# ---------------------------------------------------------------------------
# Step 1.4 - Full complaint processing pipeline
# ---------------------------------------------------------------------------
def process_complaint(text: str) -> dict:
    """Run the full NLP pipeline on a text complaint.

    Pipeline order (PII redaction MUST be first):
      1. Redact PII
      2. Analyze sentiment on redacted text
      3. Classify intent on redacted text

    Args:
        text: Raw citizen complaint text.

    Returns:
        dict with keys:
          - redacted_text (str)
          - sentiment (str)
          - confidence_scores (dict)
          - intent (str)
          - key_phrases (list)
          - pii_entities_found (int)
    """
    # TODO: Step 1.4 - Chain the pipeline functions together
    #   1. Call redact_pii(text) first
    #   2. Call analyze_sentiment() on the REDACTED text
    #   3. Call classify_intent() on the REDACTED text
    #   4. Combine all results into one dict
    raise NotImplementedError("Implement process_complaint in Step 1")
