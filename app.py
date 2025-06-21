import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load Model
model = joblib.load('uber_xgboost_model.pkl')

# Title
st.title("🚕 Uber Trip Demand Predictor")
st.write("Predict hourly Uber pickup demand in NYC based on time features.")

# Input Features
hour = st.slider("Select Hour", 0, 23, 12)
day = st.slider("Select Day of Month", 1, 31, 15)
weekday = st.selectbox("Day of Week (0 = Mon)", list(range(7)))
month = st.selectbox("Select Month", list(range(1, 13)))



# Predict Button
if st.button("Predict Trip Count"):
    input_df = pd.DataFrame([[hour, day, weekday, month]],
                            columns=['Hour', 'Day', 'Weekday', 'Month'])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Trip Count: {int(prediction)}")

# Optional: Upload and analyze CSV
st.markdown("---")
st.subheader("📁 Upload Your CSV for Batch Prediction")
uploaded_file = st.file_uploader("Choose a CSV with Hour, Day, Weekday, Month")

if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)
    preds = model.predict(user_data)
    user_data['Predicted Trips'] = preds
    st.dataframe(user_data)
