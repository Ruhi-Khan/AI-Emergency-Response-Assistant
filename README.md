🚨 AI Emergency Response Assistant

A local-first AI-powered emergency assistant that provides instant, actionable responses during critical situations — even in low-connectivity environments.

Built for the Gemma 4 Good Hackathon (Ollama Track), this system combines:

⚡ Rule-based intelligence (fast, reliable)
🤖 Local LLM (TinyLlama via Ollama)
🎤 Voice input + 🔊 voice output
📍 Location awareness (browser-based)
🌍 Problem

During emergencies, people often:

Panic and don’t know what to do
Waste time reading long AI responses
Lack access to reliable internet
💡 Solution

This assistant gives:

✅ Short, clear actions (1–2 lines)
☎️ Emergency helpline numbers (India)
🚨 Instant response (no delay, no confusion)
💻 Runs locally using Ollama (privacy + offline capability)
🧠 Architecture (Simple View)
User (Voice/Text)
        ↓
Frontend (HTML + JS)
        ↓
Flask Backend API (/chat)
        ↓
 ┌───────────────────────────┐
 │   Hybrid Intelligence     │
 │                           │
 │  1. Rule-Based System     │ → Fast fixed responses
 │  2. Ollama (TinyLlama)    │ → Smart fallback
 └───────────────────────────┘
        ↓
Short Emergency Response
📁 Project Structure
AI-Emergency-Response-Assistant/
│
├── backend/
│   ├── app.py              # Flask API
│   ├── alert_service.py    # Rule-based emergency logic
│
├── frontend/
│   ├── index.html          # UI
│   ├── style.css           # Styling
│   ├── app.js              # Voice + API logic
│
├── models/
│   └── yolov8n.pt          # (optional future vision model)
│
├── .venv/                  # Virtual environment
├── README.md
⚙️ Installation (Step-by-Step)
1. Clone Repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd AI-Emergency-Response-Assistant
2. Create Virtual Environment
python -m venv .venv
3. Activate Environment (Windows)
.\.venv\Scripts\Activate.ps1
4. Install Dependencies
pip install flask flask-cors requests
5. Install & Run Ollama Model

Download Ollama:
👉 https://ollama.com

Then run:

ollama run tinyllama
6. Start Backend Server
cd backend
python app.py

Runs on:

http://127.0.0.1:5000
7. Run Frontend

Open:

frontend/index.html

OR use Live Server:

http://127.0.0.1:5500
🚀 Features
🎤 Voice-to-text emergency input
🔊 AI voice response
📍 Location detection (browser)
⚡ Instant rule-based emergency replies
🤖 Local AI fallback (TinyLlama via Ollama)
🔐 Privacy-first (runs fully local)
🧪 Example Output

Input:

Fire in my building

Output:

🚒 Fire Emergency: Call 101 immediately. Evacuate using stairs.
🔥 Hybrid Intelligence Logic
Layer	Purpose
Rule-Based	Instant, accurate emergency actions
Ollama AI	Handles unknown/custom situations
Prompt Control	Forces short, useful responses
🌐 Why Local AI (Ollama)?
No internet dependency
Faster response
Better privacy
Perfect for disaster scenarios
⚠️ Limitations
Requires Ollama installed locally
Browser permissions needed (mic/location)
Not yet deployed (local-only)
🌟 Future Improvements
📱 Mobile app (Flutter / React Native)
🗺️ Live maps + nearest hospital/police
📷 Image-based emergency detection (YOLO)
🌐 Multi-language support
☁️ Cloud deployment (optional fallback)
🏆 Hackathon Focus

This project targets:

🌍 Global Resilience
🔐 Safety & Trust
💻 Ollama Local AI Track
👩‍💻 Author

Ruhi Khan
MSc Data Science & Big Data Analytics
Network Engineer | AI Enthusiast

📜 License

This project is open-source and free to use.
