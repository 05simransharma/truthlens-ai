from utils.gemini_client import model


def analyze_news(article):

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

    response = model.generate_content(prompt)

    return response.text