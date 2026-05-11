import streamlit as st
from engine import check_password_strength, generate_strong_password

# --- Page Config ---
st.set_page_config(page_title="CyberShield Pro", page_icon="🛡️", layout="centered")

# --- Strict CSS for Centering and Styling ---
st.markdown("""
    <style>
    /* Main Background */
    .main {
        background-color: #0e1117;
    }
    
    /* Center all button containers */
    .stButton {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }

    /* Original Button Styling */
    div.stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #0056b3;
        transform: scale(1.05);
    }

    /* Centering headings and text */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# UI Elements based on your project [cite: 1, 2, 3]
st.title("🛡️ CyberShield Pro") [cite: 1]
st.subheader("Professional Password Security Analyzer") [cite: 2]
st.write("A tool to check and generate secure passwords for your safety.") [cite: 3]

# Input Section [cite: 4]
password = st.text_input("Enter password to analyze:", type="password") [cite: 4]

if password:
    results = check_password_strength(password)
    # Strength Score Display [cite: 5]
    st.markdown(f"### Strength Score: {results['score']}/4") [cite: 5]
    
    if results['feedback']:
        st.write("#### 💡 Suggestions to improve:") [cite: 6]
        for hint in results['feedback']:
            st.warning(hint) [cite: 7, 8, 9]
    else:
        st.success("Great! This is a very strong password.")

st.divider()

# Buttons Section [cite: 10, 11]
st.markdown("### Need a Stronger Password?") [cite: 10]

# Generate Button
if st.button("🔄 Generate Strongest Password"): [cite: 11]
    st.session_state['gen_pw'] = generate_strong_password()

# Display and Instructions
if 'gen_pw' in st.session_state:
    st.code(st.session_state['gen_pw'])
    st.caption("Copy the password from the box above.")