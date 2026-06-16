import requests


def generate_ollama(prompt):

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:1.5b",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:

        return f"❌ Ollama Error:\n\n{str(e)}"