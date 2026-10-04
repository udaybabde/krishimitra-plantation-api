from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

crop_requirements = {
    "apple": {"ph_min": 5.5, "ph_max": 6.5, "temp_min": 15, "temp_max": 25, "rainfall_min": 1000, "rainfall_max": 1250,
               "note": "Needs cold climate with winter chilling hours. Best suited to hilly/temperate regions."},
    "orange": {"ph_min": 5.5, "ph_max": 7.5, "temp_min": 13, "temp_max": 37, "rainfall_min": 1000, "rainfall_max": 2000,
               "note": "Subtropical climate crop. Nagpur region especially famous for orange cultivation."},
    "mosambi": {"ph_min": 6.0, "ph_max": 7.5, "temp_min": 15, "temp_max": 35, "rainfall_min": 600, "rainfall_max": 1000,
               "note": "More drought-tolerant than orange. Warm subtropical climate preferred."},
    "mango": {"ph_min": 5.5, "ph_max": 7.5, "temp_min": 24, "temp_max": 30, "rainfall_min": 750, "rainfall_max": 2500,
               "note": "Needs distinct dry and wet seasons. Konkan region (Maharashtra) famous for Alphonso mango."},
    "banana": {"ph_min": 5.5, "ph_max": 7.0, "temp_min": 15, "temp_max": 35, "rainfall_min": 1500, "rainfall_max": 2500,
               "note": "Needs high humidity and consistent water supply. Jalgaon is a major banana belt in Maharashtra."},
    "grapes": {"ph_min": 6.0, "ph_max": 7.0, "temp_min": 15, "temp_max": 35, "rainfall_min": 500, "rainfall_max": 800,
               "note": "Needs low humidity, warm dry climate. Nashik is India's grape capital."},
    "pomegranate": {"ph_min": 5.5, "ph_max": 7.5, "temp_min": 15, "temp_max": 38, "rainfall_min": 500, "rainfall_max": 800,
               "note": "Highly drought-tolerant. Solapur district is a major pomegranate belt."},
    "papaya": {"ph_min": 6.0, "ph_max": 6.5, "temp_min": 22, "temp_max": 32, "rainfall_min": 1000, "rainfall_max": 1500,
               "note": "Needs warm climate and well-drained soil, frost-sensitive."},
    "coconut": {"ph_min": 5.5, "ph_max": 7.5, "temp_min": 20, "temp_max": 32, "rainfall_min": 1500, "rainfall_max": 2500,
               "note": "Coastal humid climate preferred (e.g. Konkan coast)."},
    "coffee": {"ph_min": 6.0, "ph_max": 6.5, "temp_min": 15, "temp_max": 28, "rainfall_min": 1500, "rainfall_max": 2500,
               "note": "Needs shade, cool humid climate, usually grown at higher elevations."},
    "cashew": {"ph_min": 4.5, "ph_max": 6.5, "temp_min": 20, "temp_max": 35, "rainfall_min": 1000, "rainfall_max": 2000,
               "note": "Grows well in coastal and lateritic soils, Konkan region suitable."},
    "guava": {"ph_min": 4.5, "ph_max": 8.2, "temp_min": 15, "temp_max": 35, "rainfall_min": 1000, "rainfall_max": 2000,
               "note": "Very hardy crop, tolerates a wide pH and climate range."},
    "chikoo": {"ph_min": 6.0, "ph_max": 8.0, "temp_min": 20, "temp_max": 35, "rainfall_min": 1250, "rainfall_max": 2500,
               "note": "Sapota. Grows well in coastal Maharashtra (Dahanu, Thane belt)."},
    "custard_apple": {"ph_min": 6.0, "ph_max": 7.5, "temp_min": 20, "temp_max": 35, "rainfall_min": 600, "rainfall_max": 1000,
               "note": "Sitaphal. Drought-tolerant, suited to semi-arid Maharashtra."},
    "lemon": {"ph_min": 5.5, "ph_max": 7.5, "temp_min": 13, "temp_max": 37, "rainfall_min": 1000, "rainfall_max": 1800,
               "note": "Similar requirements to orange, subtropical/tropical climate."},
    "fig": {"ph_min": 6.0, "ph_max": 7.5, "temp_min": 15, "temp_max": 35, "rainfall_min": 600, "rainfall_max": 900,
               "note": "Anjeer. Pune district (Purandar) is a major fig-growing region."},
    "jackfruit": {"ph_min": 6.0, "ph_max": 7.5, "temp_min": 21, "temp_max": 32, "rainfall_min": 1500, "rainfall_max": 2500,
               "note": "Needs warm humid tropical climate, common in Konkan."},
    "drumstick": {"ph_min": 6.3, "ph_max": 7.0, "temp_min": 20, "temp_max": 35, "rainfall_min": 500, "rainfall_max": 1500,
               "note": "Moringa. Very hardy, drought-tolerant, grows in most soils."},
    "tamarind": {"ph_min": 5.5, "ph_max": 8.0, "temp_min": 20, "temp_max": 35, "rainfall_min": 500, "rainfall_max": 1500,
               "note": "Chinch. Hardy perennial tree, tolerates poor soils."},
    "sugarcane": {"ph_min": 6.0, "ph_max": 7.5, "temp_min": 20, "temp_max": 35, "rainfall_min": 1000, "rainfall_max": 1500,
               "note": "Needs high water availability; major crop in Western Maharashtra (Kolhapur, Sangli)."},
    "cotton": {"ph_min": 6.0, "ph_max": 8.0, "temp_min": 21, "temp_max": 35, "rainfall_min": 600, "rainfall_max": 1000,
               "note": "Widely grown in Vidarbha and Marathwada regions of Maharashtra."},
    "soybean": {"ph_min": 6.0, "ph_max": 7.5, "temp_min": 20, "temp_max": 30, "rainfall_min": 600, "rainfall_max": 1000,
               "note": "Major Kharif crop in Vidarbha and Marathwada."},
    "turmeric": {"ph_min": 5.5, "ph_max": 7.5, "temp_min": 20, "temp_max": 30, "rainfall_min": 1500, "rainfall_max": 2250,
               "note": "Needs warm humid climate and well-drained soil."},
    "ginger": {"ph_min": 5.5, "ph_max": 6.5, "temp_min": 19, "temp_max": 28, "rainfall_min": 1500, "rainfall_max": 2500,
               "note": "Needs partial shade and high humidity."},
    "watermelon": {"ph_min": 6.0, "ph_max": 6.8, "temp_min": 24, "temp_max": 32, "rainfall_min": 400, "rainfall_max": 600,
               "note": "Warm season crop, needs well-drained sandy loam soil."},
    "muskmelon": {"ph_min": 6.0, "ph_max": 6.8, "temp_min": 24, "temp_max": 32, "rainfall_min": 400, "rainfall_max": 600,
               "note": "Similar needs to watermelon, warm dry climate."},
    "chickpea": {"ph_min": 6.0, "ph_max": 7.5, "temp_min": 10, "temp_max": 30, "rainfall_min": 400, "rainfall_max": 650,
               "note": "Chana. Major Rabi pulse crop in Maharashtra."},
    "pigeonpea": {"ph_min": 5.0, "ph_max": 7.0, "temp_min": 20, "temp_max": 30, "rainfall_min": 600, "rainfall_max": 1000,
               "note": "Tur/Arhar. Important Kharif pulse crop across Maharashtra."},
}

class SuitabilityInput(BaseModel):
    crop_name: str
    ph: float
    temperature: float
    rainfall: float

@app.get("/")
def home():
    return {"message": "KrishiMitra Plantation Suitability API is running", "supported_crops": list(crop_requirements.keys())}

@app.post("/check-suitability")
def check_suitability(data: SuitabilityInput):
    crop = data.crop_name.lower().strip().replace(" ", "_")
    req = crop_requirements.get(crop)

    if not req:
        return {
            "error": f"'{data.crop_name}' is not supported.",
            "supported_crops": list(crop_requirements.keys())
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
