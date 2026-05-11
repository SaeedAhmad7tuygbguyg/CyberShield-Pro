import streamlit as st
from engine import get_password_report, generate_secure_password

# 1. Page Config
st.set_page_config(page_title="CyberShield Pro", page_icon="🛡️", layout="centered")

# 2. VIP Styling
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .center-text { text-align: center; color: #f0f2f6; font-size: 22px; font-weight: bold; margin-bottom: 10px; }
    [data-testid="stTextInput"] { width: 90% !important; margin: 0 auto !important; }
    .stTextInput > div > div > input {
        background-color: #1a1d24 !important;
        color: white !important; 
        text-align: center;
        border: 2px solid #3e4451 !important;
        border-radius: 12px !important;
        font-size: 18px;
    }
    .metric-card {
        background-color: #1a1d24; padding: 15px; border-radius: 10px;
        text-align: center; border: 1px solid #3e4451;
    }
    .device-name { color: #00f2fe; font-weight: bold; font-size: 16px; }
    .crack-val { color: #ff4b4b; font-size: 18px; font-weight: bold; }
    
    div.stButton > button {
        width: 100%;
        background-image: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%);
        color: black; font-weight: bold; border-radius: 10px; border: none; padding: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialization
if "report_data" not in st.session_state:
    st.session_state.report_data = None
if "last_password" not in st.session_state:
    st.session_state.last_password = ""

# Header
st.markdown("<h1 style='text-align: center; color: #00f2fe;'>🔐 CYBERSHIELD PRO</h1>", unsafe_allow_html=True)
st.write("##")
st.markdown("<div class='center-text'>Secret Password Analyzer</div>", unsafe_allow_html=True)

# --- Password Input ---
password = st.text_input("", type="password", placeholder="Type your password here...", key="pass_input")

# Smart Button Logic
if not password and st.session_state.report_data is None:
    st.button("ENTER")
else:
    btn_label = "📋 COPY PASSWORD" if st.session_state.report_data else "ENTER"
    
    if st.button(btn_label):
        if not st.session_state.report_data:
            st.session_state.last_password = password
            st.session_state.report_data = get_password_report(password)
            st.rerun()
        else:
            st.code(st.session_state.last_password)
            st.toast("Password Copied!")

# 4. Results Section (Persistent)
if st.session_state.report_data:
    report = st.session_state.report_data
    score = report['score']
    
    status = ["CRITICAL", "WEAK", "MEDIUM", "STRONG", "STRONGEST"]
    colors = ["#ff4b4b", "#ffa500", "#ffee00", "#7FFF00", "#00f2fe"]
    
    st.markdown(f"<h2 style='text-align: center; color: {colors[score]};'>{status[score]}</h2>", unsafe_allow_html=True)
    st.progress((score + 1) * 20)
    st.markdown(f"<p style='text-align: right; color: white; font-size: 12px;'>Security Range: {(score+1)*20}%</p>", unsafe_allow_html=True)

    # --- Strongest Generator ---
    st.write("##")
    st.markdown("<h3 style='text-align: center;'>Generate <span style='color: #00f2fe;'>Strongest</span> Password</h3>", unsafe_allow_html=True)
    if st.button("GENERATE NEW STRONGEST PASSWORD"):
        new_p = generate_secure_password()
        st.code(new_p)
        st.balloons()

    # --- Hardware Comparison (Emoji Removed) ---
    st.write("---")
    st.markdown("<h3 style='text-align: center; color: white;'>Brute-Force Hardware Comparison</h3>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='metric-card'><p class='device-name'>Laptop</p><p class='crack-val'>{report['crack_times_display']['online_throttling_100_per_hour']}</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card' style='border-color: #ffa500;'><p class='device-name'>Gaming GPU</p><p class='crack-val'>{report['crack_times_display']['offline_slow_hashing_1e4_per_second']}</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card' style='border-color: #ff4b4b;'><p class='device-name'>Supercomputer</p><p class='crack-val'>{report['crack_times_display']['offline_fast_hashing_1e10_per_second']}</p></div>", unsafe_allow_html=True)

    # --- White Suggestions ---
    if report['feedback']['suggestions']:
        st.write("---")
        st.markdown("<p style='color: white; font-weight: bold; font-size: 18px;'>🛡️ Security Suggestions:</p>", unsafe_allow_html=True)
        for s in report['feedback']['suggestions']:
            st.markdown(f"<p style='color: white; margin-left: 15px;'>✅ {s}</p>", unsafe_allow_html=True)