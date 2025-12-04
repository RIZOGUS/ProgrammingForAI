from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

# NHTSA vPIC API Base URL
NHTSA_BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/vin/<vin>', methods=['GET'])
def decode_vin(vin):
    """
    Decodes a VIN using the NHTSA API.
    """
    try:
        # Format: https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/<vin>?format=json
        url = f"{NHTSA_BASE_URL}/decodevin/{vin}?format=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract relevant fields to make the response cleaner
        results = data.get('Results', [])
        vehicle_info = {}
        
        # Key fields we want to extract
        target_fields = [
            "Make", "Model", "Model Year", "Vehicle Type", 
            "Body Class", "Drive Type", "Fuel Type - Primary", 
            "Engine Cylinders", "Engine HP", "Plant Country", "Plant City"
        ]

        for item in results:
            variable = item.get('Variable')
            value = item.get('Value')
            if variable in target_fields and value:
                vehicle_info[variable] = value
        
        # If no specific info found, return raw results (or handle error)
        if not vehicle_info:
             return jsonify({
                "status": "error",
                "message": "Could not decode VIN or invalid VIN provided.",
                "raw_data": results
            }), 400

        return jsonify({
            "status": "success",
            "vin": vin,
            "data": vehicle_info
        })

    except requests.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 503
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/makes', methods=['GET'])
def get_makes():
    """
    Returns a list of all vehicle makes (limited to passenger cars for brevity).
    """
    try:
        # Get all makes for passenger cars to keep list manageable
        # https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/car?format=json
        url = f"{NHTSA_BASE_URL}/GetMakesForVehicleType/car?format=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        makes = [item['MakeName'] for item in data.get('Results', [])]
        
        return jsonify({
            "status": "success",
            "count": data.get('Count'),
            "makes": makes[:100] # Limit to top 100 to avoid huge payload
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/models/<make>/<year>', methods=['GET'])
def get_models(make, year):
    """
    Get models for a specific make and year.
    """
    try:
        # https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/<make>/modelyear/<year>?format=json
        url = f"{NHTSA_BASE_URL}/getmodelsformakeyear/make/{make}/modelyear/{year}?format=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        models = [item['Model_Name'] for item in data.get('Results', [])]
        
        return jsonify({
            "status": "success",
            "make": make,
            "year": year,
            "count": data.get('Count'),
            "models": models
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
