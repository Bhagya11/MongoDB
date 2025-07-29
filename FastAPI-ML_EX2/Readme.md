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

```
<img width="1357" height="647" alt="1" src="https://github.com/user-attachments/assets/00d35f79-1a2a-4459-82c9-465a80c3128a" />
<img width="1256" height="638" alt="2" src="https://github.com/user-attachments/assets/0737b6f9-b3ca-43c7-bdc3-ca5c8ff399f1" />

<img width="1361" height="696" alt="3" src="https://github.com/user-attachments/assets/f8d4c52c-4e1a-48d9-9319-f0769c4ae430" />



{
  "prediction": "DrugY",
  "status": "Prediction successful and stored in MongoDB."
}
```
