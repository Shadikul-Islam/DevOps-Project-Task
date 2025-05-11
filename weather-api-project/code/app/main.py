from flask import Flask, jsonify
import socket
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def weatherdata():
    weather_data = get_weather()
    return jsonify({
        "hostname": "server1",
        "datetime": datetime.now().strftime("%y%m%d%H%M"),
        "version": "1.0",
        "weather": {
            "dhaka": weather_data
        }
    })

def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=23.8103&longitude=90.4125&current_weather=true"
        response = requests.get(url, timeout=5)
        data = response.json()
        temperature = data["current_weather"]["temperature"]
        return {"temperature": str(temperature), "temp_unit": "c"}
    except Exception as e:
        return {"temperature": "N/A", "temp_unit": "c", "error": str(e)}

@app.route('/api/health', methods=['GET'])
def health_check():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=23.8103&longitude=90.4125&current_weather=true"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return jsonify({"status": "healthy"})
        else:
            return jsonify({"status": "unhealthy"})
    except:
        return jsonify({"status": "unhealthy"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
