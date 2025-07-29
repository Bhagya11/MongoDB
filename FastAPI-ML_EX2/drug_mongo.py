from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
from pymongo import MongoClient
from datetime import datetime

# Load the trained model
model = load("Model/drug_pipeline.joblib")

# MongoDB Compass (local) connection
client = MongoClient("mongodb://localhost:27017/")
db = client["DrugDB"]
collection = db["Predictions"]

# FastAPI app
app = FastAPI()

# Input schema
class DrugInput(BaseModel):
    Age: float
    Sex: str
    BP: str
    Cholesterol: str
    Na_to_K: float

@app.get("/")
def home():
    return {"message": "Drug Prediction API running!"}

@app.post("/predict")
def predict(data: DrugInput):
    input_data = [[
        data.Age,
        data.Sex,
        data.BP,
        data.Cholesterol,
        data.Na_to_K
    ]]

    prediction = model.predict(input_data)[0]

    # Save to MongoDB
    record = {
        "Age": data.Age,
        "Sex": data.Sex,
        "BP": data.BP,
        "Cholesterol": data.Cholesterol,
        "Na_to_K": data.Na_to_K,
        "Prediction": prediction,
        "Timestamp": datetime.utcnow()
    }

    collection.insert_one(record)

    return {
        "prediction": prediction,
        "message": "Saved to MongoDB Compass ✅"
    }
