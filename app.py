import streamlit as st
import matplotlib.pyplot as plt
from ecg_simulator import generate_ecg
from sp02_simulator import generate_spo2_wave
from utils import predict_status

st.set_page_config(page_title="Vital Sign Monitor", layout="wide")
st.title("🩺 Vital Sign Monitor")

# Sidebar inputs
st.sidebar.header("Adjust Vital Signs")

# NIBP
systolic = st.sidebar.slider("Systolic Pressure (mmHg)", 80, 200, 120)
diastolic = st.sidebar.slider("Diastolic Pressure (mmHg)", 50, 130, 80)

# Temperature
temperature = st.sidebar.slider("Body Temperature (°C)", 34.0, 41.0, 36.8, 0.1)

# SpO2
spo2 = st.sidebar.slider("SpO₂ Level (%)", 80, 100, 98)

# ECG Heart Rate (affects waveform)
heart_rate = st.sidebar.slider("Heart Rate (bpm)", 40, 180, 75)

# Display metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Systolic", systolic)
col2.metric("Diastolic", diastolic)
col3.metric("Temperature", f"{temperature:.1f} °C")
col4.metric("SpO₂", f"{spo2}%")

# Prediction
status = predict_status(systolic, diastolic, temperature, spo2, heart_rate)
st.subheader("🧠 Predicted Health Status:")
st.success(status if status == "Healthy" else f"⚠️ {status}")

# ECG & SpO₂ Plots
st.subheader("📈 Waveform Visuals")
ecg_data = generate_ecg(heart_rate)
spo2_wave = generate_spo2_wave()

fig1, ax1 = plt.subplots()
ax1.plot(ecg_data, color='red')
ax1.set_title(f"ECG Waveform (HR: {heart_rate} bpm)")
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
ax2.plot(spo2_wave, color='blue')
ax2.set_title("SpO₂ Waveform")
st.pyplot(fig2)
