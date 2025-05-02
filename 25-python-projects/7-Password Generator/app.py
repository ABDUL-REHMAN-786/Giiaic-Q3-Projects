import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.set_page_config(page_title="🔐 Password Generator", layout="centered")

st.title("🔐 Password Generator")
st.write("Customize your password below:")

# Sidebar or main area
length = st.slider("Password Length", min_value=4, max_value=50, value=12)

use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Numbers", value=True)
use_symbols = st.checkbox("Include Symbols (!@#$%^)", value=True)

if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    st.success("Generated Password:")
    st.code(password, language="text")

