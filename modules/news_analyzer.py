from utils.gemini_client import get_model


def analyze_news(article, api_key, language="English"):

    if not article.strip():
        return "❌ Please enter a news article."

    model = get_model(api_key)

    prompt = f"""
Respond ONLY in {language}.

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

        if hasattr(response, "candidates") and response.candidates:

            candidate = response.candidates[0]

            if (
                hasattr(candidate, "content")
                and candidate.content
                and hasattr(candidate.content, "parts")
                and candidate.content.parts
            ):

                output = []

                for part in candidate.content.parts:

                    if hasattr(part, "text"):
                        output.append(part.text)

                if output:
                    return "\n".join(output)

        return (
            "⚠️ Gemini returned an empty response.\n\n"
            "Possible causes:\n"
            "- Input was too large\n"
            "- Gemini blocked the response\n"
            "- Temporary API issue"
        )

    except Exception as e:
        return f"❌ Error while analyzing article:\n\n{str(e)}"