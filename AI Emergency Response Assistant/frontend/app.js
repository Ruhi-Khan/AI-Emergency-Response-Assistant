// 🎤 VOICE INPUT
function startVoice() {
    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Speech recognition not supported in this browser");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-IN";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => {
        console.log("🎤 Listening...");
    };

    recognition.onresult = function (event) {
        const text = event.results[0][0].transcript;
        document.getElementById("userInput").value = text;
    };

    recognition.onerror = function (event) {
        console.log("Mic error:", event.error);

        if (event.error === "not-allowed") {
            alert("Allow microphone permission");
        } else {
            alert("Mic error: " + event.error);
        }
    };

    recognition.onend = () => {
        console.log("🎤 Stopped");
    };

    recognition.start();
}


// 🔊 TEXT TO SPEECH
function speakText(text) {
    if (!text || text.trim() === "") return;

    // Stop previous speech
    window.speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-IN";
    speech.rate = 1;

    window.speechSynthesis.speak(speech);
}


// 📍 LOCATION
function getLocation() {
    if (!navigator.geolocation) {
        console.log("No location support");
        return;
    }

    navigator.geolocation.getCurrentPosition(
        (pos) => {
            console.log("📍 Location:", pos.coords.latitude, pos.coords.longitude);
        },
        (err) => {
            console.log("Location error:", err.message);
        }
    );
}


// 🚨 SEND DATA
async function sendData() {
    const text = document.getElementById("userInput").value.trim();
    const button = document.getElementById("helpBtn");

    if (!text) {
        alert("Enter emergency message");
        return;
    }

    // 🔴 Button click effect
    button.innerText = "Sending...";
    button.style.opacity = "0.7";

    // 📍 Get location when clicked
    getLocation();

    // ✅ Show popup
    const popup = document.getElementById("popup");
    popup.style.display = "block";

    // Auto hide popup after 2 sec
    setTimeout(() => {
        popup.style.display = "none";
    }, 2000);

    try {
        const res = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: text })
        });

        if (!res.ok) {
            throw new Error("Server error");
        }

        const data = await res.json();

        const output = data.reply || data.error || "No response";

        document.getElementById("responseBox").innerText = output;

        // 🔊 Speak response
        speakText(output);

    } catch (err) {
        console.log(err);
        alert("Backend not connected");
    }

    // 🔁 Reset button
    button.innerText = "Get Help";
    button.style.opacity = "1";
}