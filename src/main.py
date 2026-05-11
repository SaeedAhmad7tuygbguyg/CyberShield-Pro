import streamlit as st
import sys
import os

# System path set kar rahe hain taake 'src' folder ki files mil saken
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from src.engine import check_password_strength, generate_strong_password
except ImportError:
    from engine import check_password_strength, generate_strong_password

# --- Page Config ---
st.set_page_config(page_title="CyberShield Pro", page_icon="🛡️", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
    }
    .main {
        background-color: #0e1117;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ CyberShield Pro")
st.write("Professional Password Security Analyzer & Generator")

# --- Input Section ---
password = st.text_input("Enter password to analyze:", type="password")

if password:
    results = check_password_strength(password)
    st.subheader(f"Strength Score: {results['score']}/4")
    
    # Feedback loop
    if results['feedback']:
        for hint in results['feedback']:
            st.warning(hint)
    else:
        st.success("Great! This is a very strong password.")

st.divider()

# --- Buttons Section (Centered) ---
st.write("### Need a Stronger Password?")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🔄 Generate Strongest Password"):
        st.session_state['new_pw'] = generate_strong_password()

if 'new_pw' in st.session_state:
    st.code(st.session_state['new_pw'], language="")
    
    # Center the copy tip
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.info("⬆️ Copy the password from the box above")