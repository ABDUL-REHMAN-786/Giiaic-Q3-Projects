import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import sqlite3
import requests
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Title and Header
st.title("Streamlit Crash Course 🚀")
st.header("Build Data-Driven Python Web Apps in Minutes!")

# Session State Example
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
st.write(f"Counter: {st.session_state.counter}")

# Text Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Buttons
if st.button("Click Me!"):
    st.success("Button Clicked!")

# Checkbox
agree = st.checkbox("I agree")
if agree:
    st.info("You agreed!")

# Slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age: {age}")

# Progress Bar
st.subheader("Progress Bar Example")
progress_bar = st.progress(0)
for percent in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent + 1)
st.success("Completed!")

# DataFrame
st.subheader("Sample Data Table")
data = {"Name": ["Alice", "Bob", "Charlie"], "Score": [85, 90, 78]}
df = pd.DataFrame(data)
st.dataframe(df)

# Matplotlib Chart
st.subheader("Sine Wave Plot")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(df)

# Form Example
with st.form("my_form"):
    form_name = st.text_input("Enter your name")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Hello, {form_name}!")

# Database Integration
st.subheader("SQLite Database Example")
conn = sqlite3.connect("data.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()

new_user = st.text_input("Add a new user:")
if st.button("Save to Database"):
    c.execute("INSERT INTO users (name) VALUES (?)", (new_user,))
    conn.commit()
    st.success("User saved!")

c.execute("SELECT * FROM users")
data = c.fetchall()
conn.close()

st.write("Stored Users:")
st.table(data)

# API Call Example with Error Handling
st.subheader("Fetch Data from an API")
api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
def fetch_data():
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error("Failed to fetch data")
        return None

data = fetch_data()
if data:
    st.write("Bitcoin Price (USD):", data["bitcoin"]["usd"])

# Machine Learning Integration
st.subheader("Machine Learning Model Example")
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)
joblib.dump(model, "model.pkl")

y_pred = model.predict(X_test_scaled)
st.write("Model Prediction Example:")
st.write(f"Predicted value: {y_pred[0]:.2f}")

# Authentication Example
st.subheader("User Authentication")
users = {"admin": "password123", "user": "pass456"}
username = st.text_input("Username:")
password = st.text_input("Password:", type="password")
if st.button("Login"):
    if username in users and users[username] == password:
        st.success("Login successful!")
    else:
        st.error("Invalid credentials!")
