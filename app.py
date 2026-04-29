import streamlit as st
import joblib
import numpy as np

st.title("Employee Future Predictor")

model = joblib.load("attrition_model.pkl")

age = st.number_input("Age", 18, 60)
salary = st.number_input("Salary", 10000, 200000)

if st.button("Predict"):
    pred = model.predict([[age, salary]])[0]

    if pred == 1:
        loss = salary * 0.5
        st.error(f"Likely to leave. Estimated loss: ₹{loss}")
    else:
        hike = salary * 1.1
        st.success(f"Will stay. Projected salary: ₹{hike}")
