import streamlit as st
import joblib as jb
import numpy as np
from pathlib import Path

model_path = Path(__file__).resolve().parent / "energy_model.joblib"
model = jb.load(model_path)

st.title("Household Energy Forecast")

reactive_power = st.number_input("Global Reactive Power")
voltage = st.number_input("Voltage")
intensity = st.number_input("Global Intensity")
sub1 = st.number_input("Sub Metering 1")
sub2 = st.number_input("Sub Metering 2")
sub3 = st.number_input("Sub Metering 3")
hour = st.slider("Hour", 0, 23)
day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)
weekday_name = st.selectbox("Weekday", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
weekday_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
weekday = weekday_map[weekday_name]
peak_hour = 1 if 18 <= hour <= 22 else 0

if st.button("Predict"):
    input_data = np.array([[
        reactive_power,
        voltage,
        intensity,
        sub1,
        sub2,
        sub3,
        hour,
        day,
        month,
        weekday,
        peak_hour,
    ]])

    if input_data.shape[1] != getattr(model, "n_features_in_", input_data.shape[1]):
        st.error(
            f"Model expects {getattr(model, 'n_features_in_', '?')} features, but input has {input_data.shape[1]}.")
    else:
        prediction = model.predict(input_data)
        st.success(f"Predicted Energy Consumption: {prediction[0]}")
