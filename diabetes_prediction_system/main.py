from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Load the trained model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define input data model
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

# Prediction endpoint
@app.post("/predict")
def predict(diabetes: DiabetesInput):
    # Define the feature names as they were during training
    feature_names = [
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
    ]
    
    # Convert input to a DataFrame with feature names
    data = pd.DataFrame([[
        diabetes.Pregnancies, diabetes.Glucose, diabetes.BloodPressure,
        diabetes.SkinThickness, diabetes.Insulin, diabetes.BMI,
        diabetes.DiabetesPedigreeFunction, diabetes.Age
    ]], columns=feature_names)
    
    # Make prediction
    prediction = model.predict(data)[0]
    
    # Map prediction to human-readable label
    result = "diabetic" if prediction == 1 else "non diabetic"
    
    return {"prediction": result}

