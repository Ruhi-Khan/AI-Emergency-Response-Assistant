def get_alert(text, detected_objects=None):
    text = text.lower()

    # 🔥 Fire
    if "fire" in text:
        return "🚒 Fire Emergency: Call 101 immediately. Evacuate and use stairs."

    # 🚑 Medical
    elif any(word in text for word in ["fever", "headache", "pain", "injury", "blood", "unconscious"]):
        return "🚑 Medical Emergency: Call 102. Give first aid and stay calm."

    # 🚗 Accident
    elif "accident" in text:
        return "🚑 Accident: Call ambulance (102) and police (100). Check injuries."

    # 🌊 Flood
    elif "flood" in text:
        return "🌊 Flood Alert: Move to higher ground. Avoid water currents. Call 1070."

    # 🌍 Earthquake
    elif "earthquake" in text:
        return "🌍 Earthquake: Take cover under a table. Stay away from windows. Call 112."

    # ⚠️ Gas leak
    elif "gas" in text:
        return "⚠️ Gas Leak: Do not use electricity. Open windows and leave area. Call 1906."

    # 🚓 Crime
    elif any(word in text for word in ["kidnap", "theft", "robbery", "attack"]):
        return "🚓 Crime Emergency: Call Police (100). Stay safe and avoid confrontation."

    # 👩 Women safety
    elif any(word in text for word in ["harassment", "unsafe", "stalker", "abuse"]):
        return "🚨 Women Safety: Call 1091 or 112. Share location with trusted contacts."

    # 🐾 Pet
    elif any(word in text for word in ["dog", "cat", "pet"]):
        return "🐾 Pet Emergency: Contact nearest vet immediately."

    # ❌ IMPORTANT: no default return here
    return None