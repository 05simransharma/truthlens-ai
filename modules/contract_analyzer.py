from utils.gemini_client import get_model


def analyze_contract(contract_text, api_key):

    # Check if PDF text extraction failed
    if not contract_text or not contract_text.strip():
        return "❌ No text could be extracted from the uploaded PDF."

    prompt = f"""
You are a legal risk analysis assistant.

Analyze the contract and return:

1. Executive Summary
2. Risk Score (0-100)
3. High Risk Clauses
4. Medium Risk Clauses
5. User Obligations
6. Final Recommendation

Contract:

{contract_text}
"""

    try:
        model = get_model(api_key)
        response = model.generate_content(prompt)

        # First try the simple accessor
        try:
            if response.text:
                return response.text
        except Exception:
            pass

        # Fallback for Gemini responses
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
            "- Contract text extraction failed\n"
            "- Input was too large\n"
            "- Gemini blocked the response\n"
            "- Temporary API issue"
        )

    except Exception as e:
        return f"❌ Error while analyzing contract:\n\n{str(e)}"