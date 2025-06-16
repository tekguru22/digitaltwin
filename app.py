import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from ecg_simulator import generate_ecg
from sp02_simulator import generate_spo2
from utils import generate_nibp, generate_temperature

st.set_page_config(page_title="Vital Sign Monitor", layout="wide")

st.title("🩺 Vital Sign Monitor Dashboard")

col1, col2, col3, col4 = st.columns(4)

# NIBP
sys, dia = generate_nibp()
col1.metric("Systolic (mmHg)", sys)
col2.metric("Diastolic (mmHg)", dia)

# Temperature
temp = generate_temperature()
col3.metric("Body Temp (°C)", f"{temp:.1f}")

# SpO2
spo2, spo2_wave = generate_spo2()
col4.metric("SpO₂ (%)", f"{spo2:.1f}")

# ECG and SpO2 waveform
st.subheader("📈 ECG and SpO₂ Waveforms")
ecg_data = generate_ecg()

fig1, ax1 = plt.subplots()
ax1.plot(ecg_data, color="red")
ax1.set_title("ECG Signal")
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
ax2.plot(spo2_wave, color="blue")
ax2.set_title("SpO₂ Waveform")
st.pyplot(fig2)
