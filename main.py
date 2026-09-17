from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Real agro-climatic requirement ranges for perennial plantation crops
crop_requirements = {
    "apple": {
        "ph_min": 5.5, "ph_max": 6.5,
        "temp_min": 15, "temp_max": 25,
        "rainfall_min": 1000, "rainfall_max": 1250,
        "note": "Needs cold climate with winter chilling hours (below 7°C) for proper fruiting. Best suited to hilly/temperate regions."
    },
    "orange": {
        "ph_min": 5.5, "ph_max": 7.5,
        "temp_min": 13, "temp_max": 37,
        "rainfall_min": 1000, "rainfall_max": 2000,
        "note": "Subtropical climate crop. Needs well-drained soil and moderate humidity."
    },
    "mosambi": {
        "ph_min": 6.0, "ph_max": 7.5,
        "temp_min": 15, "temp_max": 35,
        "rainfall_min": 600, "rainfall_max": 1000,
        "note": "More drought-tolerant than orange. Warm subtropical climate preferred."
    },
}

class SuitabilityInput(BaseModel):
    crop_name: str
    ph: float
    temperature: float
    rainfall: float

@app.get("/")
def home():
    return {"message": "KrishiMitra Plantation Suitability API is running"}

@app.post("/check-suitability")
def check_suitability(data: SuitabilityInput):
    crop = data.crop_name.lower().strip()
    req = crop_requirements.get(crop)

    if not req:
        return {
            "error": f"'{data.crop_name}' is not supported. Supported crops: apple, orange, mosambi."
        }

    issues = []
    if not (req["ph_min"] <= data.ph <= req["ph_max"]):
        issues.append(f"Soil pH should be between {req['ph_min']} and {req['ph_max']} (yours: {data.ph})")
    if not (req["temp_min"] <= data.temperature <= req["temp_max"]):
        issues.append(f"Temperature should be between {req['temp_min']}°C and {req['temp_max']}°C (yours: {data.temperature}°C)")
    if not (req["rainfall_min"] <= data.rainfall <= req["rainfall_max"]):
        issues.append(f"Rainfall should be between {req['rainfall_min']}mm and {req['rainfall_max']}mm (yours: {data.rainfall}mm)")

    suitable = len(issues) == 0

    return {
        "crop": crop,
        "suitable": suitable,
        "issues": issues if issues else ["All parameters are within suitable range."],
        "note": req["note"]
    }
