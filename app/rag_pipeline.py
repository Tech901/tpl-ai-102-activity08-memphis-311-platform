"""
RAG pipeline for Memphis 311 citizen question intake.
Reuses patterns from Activity 7 (Neighborhood Knowledge Base).

Processes citizen questions through:
  1. Knowledge base search (Azure AI Search)
  2. Grounded answer generation with citations
"""
import os

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Lazy client initialization
# ---------------------------------------------------------------------------
_search_client = None
_openai_client = None


def _get_search_client():
    """Lazily initialize the Azure AI Search client."""
    global _search_client
    if _search_client is None:
        # TODO: Uncomment and configure
        #   from azure.search.documents import SearchClient
        #   from azure.core.credentials import AzureKeyCredential
        #   _search_client = SearchClient(
        #       endpoint=os.environ["AZURE_AI_SEARCH_ENDPOINT"],
        #       index_name=os.environ.get(
        #           "AZURE_AI_SEARCH_INDEX", "memphis-311-kb"
        #       ),
        #       credential=AzureKeyCredential(
        #           os.environ["AZURE_AI_SEARCH_KEY"]
        #       ),
        #   )
        raise NotImplementedError(
            "Configure the AI Search client in Step 3"
        )
    return _search_client


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
            "Configure the Azure OpenAI client in Step 3"
        )
    return _openai_client


# ---------------------------------------------------------------------------
# Step 3.1 - Knowledge Base Search
# ---------------------------------------------------------------------------
def search_knowledge_base(query: str, top_k: int = 5) -> list:
    """Search the Memphis 311 knowledge base for relevant documents.

    Uses Azure AI Search to find documents matching the citizen's
    question. Returns the top_k most relevant results.

    Args:
        query: The citizen's question or search query.
        top_k: Number of results to return (default: 5).

    Returns:
        list of dicts, each with keys:
          - content (str): Document text
          - title (str): Document title
          - score (float): Relevance score
    """
    # TODO: Step 3.1 - Call _get_search_client().search()
    #   Pass the query string and top parameter
    #   Extract content, title, and @search.score from each result
    #   Return a list of result dicts
    raise NotImplementedError("Implement search_knowledge_base in Step 3")


# ---------------------------------------------------------------------------
# Step 3.2 - Grounded Answer Generation
# ---------------------------------------------------------------------------
def generate_grounded_answer(question: str, context: list) -> dict:
    """Generate an answer grounded in retrieved documents.

    Builds a prompt with the retrieved document context and asks
    GPT-4o to answer the question using ONLY information from
    the provided sources. Includes source citations.

    Args:
        question: The citizen's original question.
        context: List of search result dicts from search_knowledge_base.

    Returns:
        dict with keys:
          - answer (str): The generated answer
          - sources (list): List of source titles cited
          - confidence (float): Answer confidence (0.0-1.0)
          - grounded (bool): True if answer is based on retrieved docs
    """
    # TODO: Step 3.2 - Build a system prompt for grounded answering
    #   Include the context documents in the prompt
    #   Instruct the model to only use provided sources
    #   Call _get_openai_client().chat.completions.create()
    #   Parse the response for answer, sources, and grounding status
    raise NotImplementedError("Implement generate_grounded_answer in Step 3")


# ---------------------------------------------------------------------------
# Step 3.3 - Full question processing pipeline
# ---------------------------------------------------------------------------
def process_question(question: str) -> dict:
    """Run the full RAG pipeline on a citizen question.

    Pipeline:
      1. Search the knowledge base for relevant documents
      2. Generate a grounded answer with citations

    Args:
        question: The citizen's question about Memphis services.

    Returns:
        dict with keys:
          - answer (str)
          - sources (list)
          - confidence (float)
          - grounded (bool)
          - search_results_count (int)
    """
    # TODO: Step 3.3 - Chain search_knowledge_base() and generate_grounded_answer()
    #   Pass search results as context to the answer generator
    #   Include search_results_count in the output
    raise NotImplementedError("Implement process_question in Step 3")
