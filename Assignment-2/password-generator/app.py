import streamlit as st
import re
import random
import string
import hashlib
import requests
import time
from cryptography.fernet import Fernet
from datetime import datetime
import pytz

# Set Streamlit page configuration
st.set_page_config(page_title="🔒 Password Manager", layout="centered")

# AES-256 Encryption Key (Generate once and store securely)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Initialize session state for password history if not exists
if "password_history" not in st.session_state:
    st.session_state.password_history = []

# Function to check password strength
def check_password_strength(pwd):
    score = 0
    feedback = []
    if len(pwd) >= 8:
        score += 1
    else:
        feedback.append("Increase password length to at least 8 characters.")
    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")
    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")
    if re.search(r"\d", pwd):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    if re.search(r"[!@#$%^&*]", pwd):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*).")
    if score == 5:
        return "Strong", score, feedback
    elif score >= 3:
        return "Moderate", score, feedback
    else:
        return "Weak", score, feedback

# Function to generate a strong random password
def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Function to check if the password has been leaked (Have I Been Pwned API)
def check_breach(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, rest = sha1_hash[:5], sha1_hash[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
    return response.status_code == 200 and rest in response.text

st.title("🔒 Password Manager")

# Display Current Time and Temperature
st.header("📅 Current Time & Temperature - Karachi")
karachi_tz = pytz.timezone("Asia/Karachi")
current_time = datetime.now(karachi_tz).strftime("%I:%M %p, %d %B %Y")
st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🕒 {current_time}</b></div>", unsafe_allow_html=True)

try:
    weather_response = requests.get("https://wttr.in/Karachi?format=%C+%t")
    if weather_response.status_code == 200:
        temperature = weather_response.text.split()[1]
        if "°F" in temperature:
            temp_celsius = round((float(temperature.replace("°F", "")) - 32) * 5/9, 1)
            temperature = f"{temp_celsius}°C"
        st.markdown(f"<div style='text-align: center; font-size: 24px;'><b>🌡️ Karachi Temperature: {temperature}</b></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)
except:
    st.markdown("<div style='text-align: center; font-size: 24px;'><b>🌡️ Unable to fetch temperature data.</b></div>", unsafe_allow_html=True)

# Password Strength Checker
st.header("Password Strength Meter")
password = st.text_input("Enter Password:", type="password")
if password:
    with st.spinner("Analyzing password strength..."):
        time.sleep(1.5)
    strength, score, feedback = check_password_strength(password)
    st.progress(score / 5)
    st.write(f"**Strength:** {strength}")  # Display result in UI
    if strength == "Strong":
        st.success("✅ Strong Password! Well done!")
        st.balloons()
    elif strength == "Moderate":
        st.warning("⚠️ Moderate Password! Consider improving it.")
    else:
        st.error("❌ Weak Password! Please improve your password security.")
    if feedback:
        st.write("🔹 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"   - {tip}")
    if st.button("Check Breach Status"):
        with st.spinner("Checking for breaches..."):
            time.sleep(1.5)
            if check_breach(password):
                st.error("⚠️ This password has been leaked in data breaches. Please change it!")
            else:
                st.success("✅ This password has not been found in breaches!")
    st.session_state.password_history.append({"password": password, "strength": strength})

# Password Generator
st.header("Secure Password Generator")
length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
use_digits = st.checkbox("Include Numbers", value=True)
use_specials = st.checkbox("Include Special Characters", value=True)
if st.button("Generate Password"):
    with st.spinner("Generating a secure password..."):
        time.sleep(1.5)
    new_password = generate_password(length, use_digits, use_specials)
    st.code(new_password, language="plaintext")
    st.balloons()
st.write("Use a password manager to store your generated passwords securely.")

# Password History Section
st.header("📜 Password History")
st.subheader("Stored Passwords")
max_history = st.number_input("Number of Passwords to Show:", min_value=1, max_value=100, value=10)
password_search = st.text_input("Search Password History:")
if st.session_state.password_history:
    filtered_history = [entry for entry in st.session_state.password_history if password_search in entry["password"]]
    for idx, entry in enumerate(reversed(filtered_history[-max_history:])):
        with st.expander(f"🔐 Password {idx + 1}"):
            st.write(f"**Password:** `{entry['password']}`")
            st.write(f"**Strength:** {entry['strength']}")
    if st.button("Clear History"):
        st.session_state.password_history = []
        st.success("✅ Password history cleared!")
        st.rerun()
else:
    st.info("No password history available.")

# Footer
st.write("---")
st.caption("Developed by Abdul Rehman | Built with ❤️ using Streamlit | Secure Passwords Matter! 🔒")