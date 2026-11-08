import streamlit as st
import requests

# Title of the Streamlit app
st.title("Customer Churn Prediction")

# write a brief description of the app
st.write("""
This app predicts the probability of a customer churning based on their features.""")

credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
geography = st.selectbox("Geography", options=["France", "Spain", "Germany"])
gender = st.selectbox("Gender", options=["Female", "Male"])
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", min_value=0.0, value=10000.0)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
has_cr_card = st.selectbox("Has Credit Card", options=["Yes", "No"])
is_active_member = st.selectbox("Is Active Member", options=["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = {
        "CreditScore": credit_score,
        "Geography": geography,
        "Gender": gender,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_of_products,
        "HasCrCard": 1 if has_cr_card == "Yes" else 0,
        "IsActiveMember": 1 if is_active_member == "Yes" else 0,
        "EstimatedSalary": estimated_salary
    }

    # Send a POST request to the FastAPI endpoint
    response = requests.post("http://localhost:8000/predict", json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.write(f"Churn Probability: {result['churn_probability']:.2f}")
        st.write(f"Churned: {'Yes' if result['churned'] == 1 else 'No'}")
    else:
        st.write("Error in prediction. Please try again.")