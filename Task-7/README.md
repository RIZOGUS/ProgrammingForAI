# Vehicle Info API

A Flask-based backend application that provides vehicle information using the free [NHTSA vPIC API](https://vpic.nhtsa.dot.gov/api/).

## 🚀 Features

- **VIN Decoding**: Get detailed specifications (Make, Model, Year, Engine, etc.) from a VIN.
- **Make Listing**: Retrieve a list of car manufacturers.
- **Model Lookup**: Find available models for a specific Make and Year.

## 🛠️ Setup & Installation

1. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Server**:

    ```bash
    python app.py
    ```

    The server will start at `http://127.0.0.1:5000`.

## 📡 API Endpoints

### 1. Health Check

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns API status and available endpoints.

### 2. Decode VIN

- **URL**: `/api/vin/<vin>`
- **Method**: `GET`
- **Example**: `/api/vin/5UXWX7C5*BA` (Note: Real VINs are 17 chars)
- **Response**:

    ```json
    {
        "status": "success",
        "vin": "...",
        "data": {
            "Make": "BMW",
            "Model": "X3",
            "Model Year": "2011",
            "Vehicle Type": "MULTIPURPOSE PASSENGER VEHICLE (MPV)",
            ...
        }
    }
    ```

### 3. Get Makes

- **URL**: `/api/makes`
- **Method**: `GET`
- **Description**: Returns a list of passenger car manufacturers (limited to first 100 for brevity).

### 4. Get Models

- **URL**: `/api/models/<make>/<year>`
- **Method**: `GET`
- **Example**: `/api/models/honda/2020`
- **Response**:

    ```json
    {
        "status": "success",
        "make": "honda",
        "year": "2020",
        "models": ["Civic", "Accord", "CR-V", ...]
    }
    ```
