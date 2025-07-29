# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
import os

# Load dataset
df = pd.read_csv("Data/drug.csv").sample(frac=1)

X = df.drop("Drug", axis=1).values
y = df["Drug"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=125)

# Preprocessing
cat_col = [1, 2, 3]
num_col = [0, 4]

transform = ColumnTransformer([
    ("encoder", OrdinalEncoder(), cat_col),
    ("imputer", SimpleImputer(strategy="median"), num_col),
    ("scaler", StandardScaler(), num_col),
])

pipe = Pipeline([
    ("preprocessing", transform),
    ("model", RandomForestClassifier(n_estimators=10, random_state=125)),
])

pipe.fit(X_train, y_train)

# Save model
os.makedirs("Model", exist_ok=True)
dump(pipe, "Model/drug_pipeline.joblib")
print("✅ Model trained and saved to Model/drug_pipeline.joblib")
