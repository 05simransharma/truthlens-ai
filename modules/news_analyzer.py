from utils.gemini_client import get_model


def analyze_news(article, api_key):

    if not article.strip():
        return "❌ Please enter a news article."

    model = get_model(api_key)

    prompt = f"""
You are a fact-checking assistant.

Analyze this article and provide:

1. Main Claims
2. Potential Bias
3. Credibility Score (0-100)
4. Missing Information
5. Verdict

Article:

{article}
"""

    try:

        response = model.generate_content(prompt)

        try:
            if response.text:
                return response.text
        except Exception:
            pass

        return "⚠️ Gemini returned an empty response."

    except Exception as e:
        return f"❌ Error while analyzing article:\n\n{str(e)}"