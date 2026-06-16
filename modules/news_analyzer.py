from utils.gemini_client import get_model
from utils.ollama_client import generate_ollama


def analyze_news(
    article,
    api_key=None,
    language="English",
    provider="Gemini (Cloud)"
):

    if not article.strip():
        return "❌ Please enter a news article."

    article = article[:5000]

    prompt = f"""
Respond ONLY in {language}.

You are a professional fact-checking assistant.

Analyze the article and return the answer EXACTLY in this format.

# Main Claims
- Claim 1
- Claim 2

# Potential Bias
(Short explanation)

# Credibility Score
(Number between 0 and 100)

# Missing Information
- Point 1
- Point 2

# Verdict
(Brief verdict)

Article:

{article}
"""

    try:

        if provider == "Ollama (Local)":
            return generate_ollama(prompt)

        model = get_model(api_key)

        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "⚠️ Gemini returned an empty response."

    except Exception as e:

        return (
            "❌ Error while analyzing article:\n\n"
            f"{str(e)}"
        )