import streamlit as st

st.set_page_config(page_title="AI-Enabled EEG Home Automation", layout="centered")

# Title
st.title("🧠 Simulated AI-Enabled EEG Home Automation")
st.caption("Click buttons to simulate 'thought' commands decoded by AI")

st.markdown("---")

# Simulated Commands
st.subheader("🧠 Thought Commands")

col1, col2, col3 = st.columns(3)

with col1:
    light_on = st.button("💡 Turn ON Lights")

with col2:
    fan_on = st.button("🌀 Turn ON Fan")

with col3:
    ac_on = st.button("❄️ Turn ON AC")

col4, col5, col6 = st.columns(3)

with col4:
    light_off = st.button("💡 Turn OFF Lights")

with col5:
    fan_off = st.button("🛑 Turn OFF Fan")

with col6:
    ac_off = st.button("🔕 Turn OFF AC")

# Output Area
st.markdown("---")
st.subheader("🔧 System Response")

if light_on:
    st.success("🧠 AI decoded: 'Turn ON the lights' ➜ ✅ Lights are ON")

if fan_on:
    st.success("🧠 AI decoded: 'Turn ON the fan' ➜ ✅ Fan is ON")

if ac_on:
    st.success("🧠 AI decoded: 'Turn ON the AC' ➜ ✅ Air Conditioner is ON")

if light_off:
    st.warning("🧠 AI decoded: 'Turn OFF the lights' ➜ 💡 Lights are OFF")

if fan_off:
    st.warning("🧠 AI decoded: 'Turn OFF the fan' ➜ 🛑 Fan is OFF")

if ac_off:
    st.warning("🧠 AI decoded: 'Turn OFF the AC' ➜ 🔕 AC is OFF")

# Footer
st.markdown("---")
st.caption("🔄 This is a simulated interface for EEG-to-AI home automation. Real systems require EEG hardware + AI decoding.")
