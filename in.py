import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[\W_]', password):
        score += 1

    if score == 4:
        return "Strong 💪", "✅ Green"
    elif score == 3:
        return "Moderate 🔐", "🟠 Orange"
    elif score == 2:
        return "Weak 😐", "🔴 Red"
    else:
        return "Very Weak 😟", "🔴 Red"

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check how strong it is.")

password = st.text_input("Password", type="password")

if password:
    strength, color = check_password_strength(password)
    st.markdown(f"### Strength: **{strength}**")
