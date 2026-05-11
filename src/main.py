import streamlit as st
from engine import check_password_strength, generate_strong_password

# Page configuration
st.set_page_config(page_title="CyberShield Pro", page_icon="🛡️", layout="centered")

# Custom CSS for UI Enhancement
st.markdown("""
    <style>
    /* Buttons ko center alignment dene ke liye */
    div.stButton > button:first-child {
        display: block;
        margin: 0 auto;
        width: auto;
        padding-left: 30px;
        padding-right: 30px;
    }
    .main {
        background-color: #0e1117;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ CyberShield Pro")
st.subheader("Advanced Password Security Analyzer")

# User Input
password = st.text_input("Enter password to analyze:", type="password")

if password:
    results = check_password_strength(password)
    # Aapka purana analysis wala code yahan rehne dein...
    st.write(f"Strength: {results['score']}/4")

st.divider()

# --- BUTTONS SECTION (CENTERED) ---
st.write("### Need a Stronger Password?")

# Pehla button center karne ke liye columns ka use
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    if st.button("🔄 Generate New Strongest Password"):
        new_pw = generate_strong_password()
        st.session_state['generated_pw'] = new_pw

# Agar password generate ho chuka hai toh usey display aur copy button dikhayein
if 'generated_pw' in st.session_state:
    st.success(f"Generated Password: `{st.session_state['generated_pw']}`")
    
    # Copy button ko center karne ke liye columns
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        # Note: Streamlit 1.30+ mein code block ke sath copy feature khud aata hai
        # Par agar aap button chahte hain:
        st.button("📋 Copy to Clipboard")
        st.info("Tip: You can also copy from the box above!")