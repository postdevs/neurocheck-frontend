import streamlit as st
from utils.api_client import call_eeg_api

st.set_page_config(page_title="EEG Fatigue Detector", layout="centered")
st.title("NeuroCheck EEG Fatigue Detector")

uploaded_file = st.file_uploader("📂 Upload EEG data", type=["csv", "edf"])

if uploaded_file:
    # Display upload status
    st.write(f"✅ File uploaded: {uploaded_file.name}")

    # Display processing status
    with st.spinner("Analyzing EEG data..."):
        result = call_eeg_api(uploaded_file)

    # If backend offline, warn but still show fake response
    if result.get("backend_status") == "offline":
        st.warning("⚠️ Backend is offline, showing demo prediction instead.")

    # Show prediction result
    if "fatigue_class" in result:
        st.success(f"Prediction: **{result['fatigue_class']}**")
        if "confidence" in result:
            st.write(f"Confidence: {result['confidence']:.2f}")
    else:
        st.error("❌ Could not get prediction.")
