from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Simulated data for real estate analysis
properties = [
    {"id": 1, "name": "Luxury Villa", "price": 500000, "roi": 8.5},
    {"id": 2, "name": "Urban Apartment", "price": 250000, "roi": 6.8},
    {"id": 3, "name": "Country House", "price": 400000, "roi": 7.2}
]

@app.route('/properties', methods=['GET'])
def get_properties():
    return jsonify(properties)

@app.route('/analyze', methods=['POST'])
def analyze_property():
    data = request.json
    price = data.get("price", 0)
    roi = random.uniform(5, 10)  # Simulating ROI analysis
    return jsonify({"price": price, "roi": round(roi, 2)})

if __name__ == "__main__":
    app.run(debug=True)
