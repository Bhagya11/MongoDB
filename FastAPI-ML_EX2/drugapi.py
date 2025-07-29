from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# ✅ Load the model from pickle file
model = joblib.load("Model/drug_pipeline.pkl")

# FastAPI app
app = FastAPI()

# Request schema
class DrugInput(BaseModel):
    Age: int
    Sex: str
    BP: str
    Cholesterol: str
    Na_to_K: float

@app.get("/")
def home():
    return {"message": "Welcome to Drug Prediction API using Pickle!"}

@app.post("/predict/")
def predict(data: DrugInput):
    input_df = pd.DataFrame([{
        "Age": data.Age,
        "Sex": data.Sex,
        "BP": data.BP,
        "Cholesterol": data.Cholesterol,
        "Na_to_K": data.Na_to_K
    }])
    prediction = model.predict(input_df)[0]
    return {"predicted_drug": prediction}
