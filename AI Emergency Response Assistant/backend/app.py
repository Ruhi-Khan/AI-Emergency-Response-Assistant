from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from alert_service import get_alert

app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/generate"


@app.route("/")
def home():
    return "AI Emergency Backend is running"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data.get("message", "")

        # ✅ STEP 1: RULE-BASED (your alert system)
        alert = get_alert(prompt)

        if alert:
            return jsonify({"reply": alert})

        # ✅ STEP 2: OLLAMA FALLBACK
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "tinyllama",
                "prompt": f"""
You are an emergency assistant.

STRICT RULES:
- Give SHORT response (1-2 lines)
- Must follow this format exactly:
  [Emoji] Emergency: action. Call number.
- No explanation
- No extra details
- India emergency numbers only

User: {prompt}
""",
                "stream": False
            },
            timeout=20
        )

        result = response.json()
        reply = result.get("response", "").strip()

        # fallback safety
        if not reply:
            reply = "📍 Stay calm. Call emergency services (112)."

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)