import requests

def get_ai_response(text, detected_objects):
    prompt = f"""
You are an emergency assistant AI.

User says: {text}

Give:
1. What is the situation
2. Immediate steps
3. Emergency numbers (India)

Keep it short and helpful.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data["response"]

    except Exception as e:
        return "AI not available. Please check Ollama."