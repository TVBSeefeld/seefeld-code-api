from flask import Flask, jsonify
import json
import os

app = Flask(__name__)
CODES_FILE = "codes.json"

# Funktion zum Laden der Codes
def load_codes():
    if os.path.exists(CODES_FILE):
        with open(CODES_FILE, "r") as f:
            return json.load(f)
    return {"codes": []}

# Funktion zum Speichern der Codes
def save_codes(data):
    with open(CODES_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/api/get-code", methods=["GET"])
def get_code():
    data = load_codes()
    
    # Finde den ersten ungenutzten Code
    for item in data["codes"]:
        if not item["used"]:
            item["used"] = True  # Markiere Code als verwendet
            save_codes(data)  # Speichere die Änderung
            return jsonify({"success": True, "code": item["code"]})
    
    return jsonify({"success": False, "message": "Keine Codes mehr verfügbar."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
