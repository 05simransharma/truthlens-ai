from utils.gemini_client import model


def analyze_contract(contract_text):

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

    response = model.generate_content(prompt)

    return response.text