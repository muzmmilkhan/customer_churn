import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from pydantic import BaseModel
from fastapi import FastAPI

model = load_model('customer_churn_model.h5')
scaler = joblib.load('scaler.pkl')


class CustomerFeatures(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float


app = FastAPI()

geo_map = {'France': 0, 'Spain': 1, 'Germany': 2}
gender_map = {'Female': 0, 'Male': 1}

@app.post('/predict')
def predict_churn(features: CustomerFeatures):
    data = features.dict()
    # Encode categorical
    data['Geography'] = geo_map.get(data['Geography'], 0)
    data['Gender'] = gender_map.get(data['Gender'], 0)
    data = scaler.transform(pd.DataFrame([data]))
    prediction = model.predict(data)[0]
    return {'churn_probability': float(prediction[0]), 'churned': int(prediction[0] > 0.5)}