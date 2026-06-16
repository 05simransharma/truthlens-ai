import requests


def generate_ollama(prompt):

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:1.5b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2
                }
            },
            timeout=300
        )

        response.raise_for_status()

        return response.json().get(
            "response",
            "⚠️ Empty response from Ollama."
        )

    except Exception as e:

        return (
            "❌ Ollama Error:\n\n"
            f"{str(e)}"
        )