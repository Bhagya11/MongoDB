# 🚀 Drug Prediction API with FastAPI & MongoDB

This project is a machine learning API built using **FastAPI**, which predicts the type of drug a patient should take based on input features. It also stores all prediction inputs and results in **MongoDB** for tracking.

---

## 📦 Features

- Accepts input via REST API (JSON format)
- Predicts drug type using a trained ML model (`RandomForestClassifier`)
- Saves predictions and input data in **MongoDB**
- Swagger UI documentation at `/docs`

---

## 🧪 Sample Input

```json
{
  "Age": 45,
  "Sex": "M",
  "BP": "HIGH",
  "Cholesterol": "NORMAL",
  "Na_to_K": 15.5
}


git clone https://github.com/your-username/fastapi-drug-api.git
cd fastapi-drug-api

python train_model.py
uvicorn drugapi:app --reload

{
  "prediction": "DrugY",
  "status": "Prediction successful and stored in MongoDB."
}
