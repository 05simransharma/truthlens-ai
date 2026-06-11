import google.generativeai as genai


def get_model(api_key):

    if not api_key:
        raise ValueError("Please provide a Gemini API Key.")

    genai.configure(api_key=api_key)

    return genai.GenerativeModel("gemini-2.5-flash")