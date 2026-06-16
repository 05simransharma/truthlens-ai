from utils.gemini_client import get_model
from utils.ollama_client import generate_ollama


def analyze_contract(
    contract_text,
    api_key=None,
    language="English",
    provider="Gemini (Cloud)"
):

    if not contract_text or not contract_text.strip():
        return "❌ No text could be extracted from the uploaded PDF."

    contract_text = contract_text[:6000]

    prompt = f"""
Respond ONLY in {language}.

You are a legal contract risk analysis assistant.

Analyze the contract and return the result EXACTLY in this format.

# Executive Summary
(2-3 sentences)

# Risk Score
(Number between 0 and 100)

# High Risk Clauses
- Item 1
- Item 2

# Medium Risk Clauses
- Item 1
- Item 2

# User Obligations
- Item 1
- Item 2

# Final Recommendation
(Short recommendation)

Contract:

{contract_text}
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
            "❌ Error while analyzing contract:\n\n"
            f"{str(e)}"
        )