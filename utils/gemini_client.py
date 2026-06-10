import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

env_path = Path(__file__).parent.parent / ".env"

print("Looking for .env at:", env_path)

load_dotenv(env_path)

api_key = os.getenv("GOOGLE_API_KEY")

print("API Key Loaded:", api_key is not None)

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")