# 🚨 AI Emergency Response Assistant

**(Offline + Real-Time Support) Powered by Gemma 4 for Global Resilience and Life-Saving Decisions.**

A local-first AI-powered emergency assistant providing instant, actionable responses during critical situations—even in low-connectivity environments.

> **Built for the Gemma 4 Good Hackathon (Ollama Track)**

---

## 🧩 Features

- ⚡ **Rule-based intelligence** (fast, reliable)
- 🤖 **Local LLM** (TinyLlama via Ollama)
- 🎤 **Voice input** + 🔊 **voice output**
- 📍 **Location awareness** (browser-based)
- ✅ **Short, clear actions** (1–2 lines per emergency)
- ☎️ **Emergency helpline numbers** (India)
- 🚨 **Instant response** (no delay, no confusion)
- 💻 **Runs locally** using Ollama (privacy + offline)

---

## 🌍 Problem

During emergencies, people often:

- Panic and don’t know what to do
- Waste time reading long AI responses
- Lack access to reliable internet

---

## 💡 Solution

This assistant provides:

- Short, clear actions (1–2 lines)
- Emergency contact numbers
- Instant, privacy-first responses (no external servers)

---

## 🧠 Architecture (Simple View)

```
User (Voice/Text)
        │
        ▼
Frontend (HTML + JS)
        │
        ▼
Backend (Flask API /chat)
        │
        ▼
Hybrid Intelligence Layer
   ├─ Rule-Based System (fast)
   └─ Ollama (TinyLlama) (smart fallback)
        │
        ▼
Short Emergency Response
```

---

## 📁 Project Structure

```
AI-Emergency-Response-Assistant/
├── backend/
│   ├── app.py              # Flask API
│   └── alert_service.py    # Rule-based emergency logic
├── frontend/
│   ├── index.html          # UI
│   ├── style.css           # Styling
│   └── app.js              # Voice + API logic
├── models/
│   └── yolov8n.pt          # (optional future vision model)
├── .venv/                  # Virtual environment
├── README.md
```

---

## ⚙️ Installation (Step-by-Step)

1. **Clone Repository**
   ```bash
   git clone https://github.com/YogeshK34/AI-Emergency-Response-Assistant.git
   cd AI-Emergency-Response-Assistant
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate Environment (Windows)**
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```

4. **Install Dependencies**
   ```bash
   pip install flask flask-cors requests
   ```

5. **Install & Run Ollama Model**

   - Download Ollama: [https://ollama.com](https://ollama.com)
   - Run model:
     ```bash
     ollama run tinyllama
     ```

6. **Start Backend Server**
   ```bash
   cd backend
   python app.py
   ```
   Runs on: `http://127.0.0.1:5000`

7. **Run Frontend**

   - Open `frontend/index.html` in your browser  
   - OR use Live Server: `http://127.0.0.1:5500`

---

## 🧪 Example Output

**Input:**
```
Fire in my building
```
**Output:**
```
🚒 Fire Emergency: Call 101 immediately. Evacuate using stairs.
```

---

## 🔥 Hybrid Intelligence Logic

| Layer            | Purpose                               |
|------------------|---------------------------------------|
| Rule-Based       | Instant, accurate emergency actions   |
| Ollama AI        | Handles unknown/custom situations     |
| Prompt Control   | Forces short, useful responses        |

---

## 🌐 Why Local AI (Ollama)?

- No internet dependency
- Faster response
- Better privacy
- Perfect for disaster scenarios

---

## ⚠️ Limitations

- Requires Ollama installed locally
- Needs browser permissions (mic/location)
- Not yet deployed (local-only)

---

## 🌟 Future Improvements

- 📱 Mobile app (Flutter / React Native)
- 🗺️ Live maps + nearest hospital/police
- 📷 Image-based emergency detection (YOLO)
- 🌐 Multi-language support
- ☁️ Optional cloud deployment fallback

---

## 🏆 Hackathon Focus

This project targets:

- 🌍 Global Resilience
- 🔐 Safety & Trust
- 💻 Ollama Local AI Track

---

## 👩‍💻 Author

**Ruhi Khan**  
MSc Data Science & Big Data Analytics  
Network Engineer | AI Enthusiast

---

## 📜 License

This project is open-source and free to use.
