#  Uber Trip Analyzer

A **Streamlit web app** that analyzes and predicts **Uber trip demand** in New York City using real-world data and machine learning.

---

##  Features

* 📊 Visualizes Uber pickups by hour, day, and weekday
* 🔍 Performs exploratory data analysis (EDA)
* 🤖 Predicts hourly trip count using **XGBoost**
* 📅 Accepts custom CSV input
* 💻 Fully interactive via **Streamlit web interface**

---

## 🛠️ Tech Stack

| Tool/Library        | Use                       |
| ------------------- | ------------------------- |
| Python              | Programming               |
| Pandas, NumPy       | Data handling             |
| Seaborn, Matplotlib | Data visualization        |
| XGBoost, Sklearn    | ML model & evaluation     |
| Joblib              | Model saving/loading      |
| Streamlit           | Build web app             |
| Git & GitHub        | Version control + hosting |

---

##  Project Structure

```
uber-web-app/
├── app.py                     # Streamlit app code
├── uber_xgboost_model.pkl     # Trained ML model
├── sample_input.csv           # (Optional) For batch prediction
├── README.md                  # Project description
```

---

##  How It Works

1. Combines Uber NYC trip data from April–Sept 2014
2. Performs feature extraction from timestamp (hour, weekday, etc.)
3. Trains an **XGBoost Regressor** to predict hourly demand
4. Launches a web interface to input time values or CSVs
5. Outputs the predicted number of trips for each input

---

##  Demo Screenshot
![image](https://github.com/user-attachments/assets/85574291-ce4b-4522-93bb-ab9b6a4eccf3)



##  Try It Live

(https://uber-trip-analyzer-cj7dyczddgvkrfshd8ggzm.streamlit.app/)

##  Author

**Atharva Wadekar**
*Data Analyst & Machine Learning Enthusiast*
GitHub: [@AtharvaWadekar26](https://github.com/AtharvaWadekar26)

---
