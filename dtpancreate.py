import streamlit as st

# Title
st.title("🩺 Pancreas Digital Twin: Personalized Diabetes Management")

# Glucose level
glucose = st.slider("🩸 Blood Glucose Level (mg/dL)", 50, 400, 100)
st.write(f"Glucose Level: {glucose} mg/dL")

# Meal intake
meal = st.selectbox("🍽️ Meal Intake:", ["No Meal", "Low Carb", "Moderate Carb", "High Carb"])

# Exercise
exercise = st.selectbox("🏃‍♂️ Exercise:", ["None", "Light", "Moderate", "Intense"])

# Insulin dose
insulin = st.slider("💉 Insulin Dose (units):", 0, 30, 0)
st.write(f"Insulin Dose: {insulin} units")

# Medication dose (e.g., Getryl)
getryl = st.selectbox("💊 Getryl Dose:", ["None", "Half Tablet", "1 Tablet", "2 Tablets"])

# Simulate adjusted glucose based on inputs
adjusted_glucose = glucose

# Adjust glucose based on meal
if meal == "Low Carb":
    adjusted_glucose += 10
elif meal == "Moderate Carb":
    adjusted_glucose += 30
elif meal == "High Carb":
    adjusted_glucose += 50

# Adjust glucose based on exercise
if exercise == "Light":
    adjusted_glucose -= 10
elif exercise == "Moderate":
    adjusted_glucose -= 20
elif exercise == "Intense":
    adjusted_glucose -= 35

# Adjust based on insulin
adjusted_glucose -= insulin * 5

# Adjust based on Getryl
if getryl == "Half Tablet":
    adjusted_glucose -= 15
elif getryl == "1 Tablet":
    adjusted_glucose -= 30
elif getryl == "2 Tablets":
    adjusted_glucose -= 50

# Clamp result between 40 and 400
adjusted_glucose = max(40, min(adjusted_glucose, 400))

# Output result
st.markdown("---")
st.subheader("🧪 Simulation Result")
if 80 <= adjusted_glucose <= 140:
    st.success(f"✅ Normal glucose. Balanced response. (Adjusted Glucose: {adjusted_glucose} mg/dL)")
elif adjusted_glucose < 80:
    st.warning(f"⚠️ Hypoglycemia risk! (Adjusted Glucose: {adjusted_glucose} mg/dL)")
else:
    st.error(f"🚨 Hyperglycemia risk! (Adjusted Glucose: {adjusted_glucose} mg/dL)")

# Visualization bar
st.progress(min(adjusted_glucose, 400) / 400)

# Footer
st.caption("This is a simulation model for educational purposes. Consult your physician for real treatment decisions.")
