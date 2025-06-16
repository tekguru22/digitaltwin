import streamlit as st
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Kidney Digital Twin", layout="centered")

# Title
st.markdown("## 🧠 Kidney Digital Twin: Drug, EHR, & Nephron Simulation")

# Sliders for inputs
bp = st.slider("🩺 Blood Pressure (mmHg)", 90, 180, 120)
ckd_stage = st.slider("🩻 CKD Stage (1=Healthy, 5=Severe)", 1, 5, 3)
creatinine = st.slider("🧪 Serum Creatinine (mg/dL)", 0.5, 6.0, 1.5)
diuretic_dose = st.slider("💊 Loop Diuretic Dose (0=None, 1=Full)", 0.0, 1.0, 0.4)

# GFR Calculation (simplified estimate)
gfr = max(5, int(120 / creatinine) - (ckd_stage * 10))  # Basic eGFR model
urine_output = max(100, int(gfr * 10 + diuretic_dose * 200))  # Simple urine model

# Display estimates
st.markdown(f"🧮 **Estimated GFR**: `{gfr} mL/min`")
st.markdown(f"💧 **Estimated Urine Output**: `{urine_output} mL/day`")

# Visual Output
fig, ax = plt.subplots(figsize=(4, 4))
circle = plt.Circle((0.5, 0.5), 0.4, color='lightblue', alpha=0.6)
ax.add_artist(circle)
ax.text(0.5, 0.7, f"GFR:\n{gfr} mL/min", fontsize=12, ha='center')
ax.text(0.5, 0.3, f"Urine:\n{urine_output} mL/day", fontsize=12, ha='center')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("📌 *Drug, BP, CKD => Twin Response Simulation*")

# Contact / Collaboration
st.info("🤝 Interested in developing organ Digital Twins or AI-healthcare tools? Let's collaborate!")
