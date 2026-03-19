import os
import streamlit as st
import pickle
import numpy as np

# Ensure the model is loaded relative to this script's directory.
model_path = os.path.join(os.path.dirname(__file__), "energy_model.pkl")
model = pickle.load(open(model_path, "rb"))

st.title("Household Energy Forecast")

voltage = st.number_input("Voltage")
intensity = st.number_input("Intensity")
hour = st.slider("Hour",0,23)

if st.button("Predict"):
    
    input_data = np.array([[voltage,intensity,hour]])
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Energy Consumption: {prediction[0]}") 
