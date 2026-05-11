import streamlit as st
# Simple import kyunke dono files ab ek hi folder mein hain
from engine import check_password_strength, generate_strong_password

# --- Page Configuration ---
st.set_page_config(page_title="CyberShield Pro", page_icon="🛡️", layout="centered")

# --- Custom CSS for Centering & Colors ---
st.markdown("""
    <style>
    /* Buttons ko darmiyan mein lane ke liye */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: bold;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #0056b3;
    }
    /* Overall padding */
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ CyberShield Pro")
st.subheader("Professional Password Security Analyzer")
st.write("A tool to check and generate secure passwords for your safety.")

# --- Input Section ---
password = st.text_input("Enter password to analyze:", type="password", help="Analyze any password for security flaws.")

if password:
    results = check_password_strength(password)
    
    # Display Score
    score = results['score']
    colors = ["#ff4b4b", "#ffa500", "#ffff00", "#90ee90", "#00ff00"]
    st.markdown(f"<h3 style='text-align: center; color: {colors[score]};'>Strength Score: {score}/4</h3>", unsafe_allow_html=True)
    
    # Feedback hints
    if results['feedback']:
        st.write("### 💡 Suggestions to improve:")
        for hint in results['feedback']:
            st.info(hint)
    else:
        st.success("🔥 Excellent! This is a bulletproof password.")

st.divider()

# --- Password Generator (Centered) ---
st.write("### 🛠️ Need a Stronger Password?")

# Centering with columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🔄 Generate Strongest Password"):
        st.session_state['generated_pw'] = generate_strong_password()

# Display results
if 'generated_pw' in st.session_state:
    st.markdown("---")
    st.write("**Your Secure Password:**")
    st.code(st.session_state['generated_pw'], language="")
    st.caption("☝️ Copy this password and use it securely.")