import streamlit as st
import time

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="centered")

# ---------- APPLE-STYLE MODERN WHITE THEME ----------
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(120deg, #f7faff 85%, #e7eaf7 100%) !important;
    }
    .jarvis-glass {
        margin: 50px auto 0 auto;
        background: rgba(255,255,255,0.88);
        border-radius: 24px;
        box-shadow: 0 10px 36px 0 #6073e21a, 0 2px 8px #dee5ff24;
        backdrop-filter: blur(12px);
        padding: 2.6em 2.1em 2.2em 2.1em;
        max-width: 500px;
        min-width: 310px;
        border: 1.5px solid #e9eaf7;
        transition: box-shadow 0.3s;
    }
    .jarvis-glass:hover {
        box-shadow: 0 14px 64px 0 #6b7cf650, 0 2px 8px #7ca6ff14;
        border: 1.6px solid #8fb3ff14;
    }
    .jarvis-header {
        font-size: 2.2em;
        font-family: 'SF Pro Display', 'Inter', 'Montserrat', sans-serif;
        background: linear-gradient(87deg,#1767ff 20%,#3ea4ea 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900;
        letter-spacing: 2.2px;
        margin-bottom: 12px;
        text-align: center;
    }
    .subtext {
        color: #8692b2; text-align: center; margin-bottom: 2.2em;
        font-family: 'Inter', sans-serif;
        font-size: 1.13em;
        letter-spacing: 1.4px;
    }
    .input-bar {
        width: 100%; font-size: 1.16em;
        padding: 1.1em 1.1em 1.1em 1.3em;
        border-radius: 13px;
        border: 1.4px solid #c9caff7a;
        outline: none;
        margin-bottom: 28px;
        background: rgba(245,246,252,0.94);
        color: #23243b;
        font-family: 'Inter', 'Montserrat', sans-serif;
        box-shadow: 0 2px 18px #b6b4fc13;
        transition: border 0.23s, box-shadow 0.23s;
    }
    .input-bar:focus {
        border: 2.3px solid #5a90ff;
        background: #fff;
        box-shadow: 0 0 12px #c0cfff44;
    }
    .ai-answer-bubble {
        margin: 38px auto 0 auto;
        background: linear-gradient(98deg,#fafdff 65%,#e3eaff 100%);
        color: #304268;
        border-radius: 16px;
        box-shadow: 0 2px 22px #adb0c633;
        font-size: 1.14em;
        font-family: 'Inter', 'Montserrat', sans-serif;
        padding: 1.27em 1.45em;
        animation: fadeIn 1.1s;
        border: 1.4px solid #e1e4f7;
    }
    @keyframes fadeIn {
        0% {opacity:0; transform:translateY(22px);}
        100% {opacity:1; transform:translateY(0);}
    }
    .footer-glass {
        margin-top: 70px;
        color: #8599c3c5;
        font-size: 1em;
        text-align:center;
        font-family: 'Inter',sans-serif;
        letter-spacing: 1.5px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css?family=Inter:400,700|Montserrat:700" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown('<div class="jarvis-glass">', unsafe_allow_html=True)
st.markdown('<div class="jarvis-header">Jarvis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Your minimal, premium AI assistant</div>', unsafe_allow_html=True)

search = st.text_input(
    "Ask Jarvis anything...",
    key="search_input",
    placeholder="Try: How do I backup my Linux database?",
    label_visibility="visible",
)

st.markdown('</div>', unsafe_allow_html=True)

if "answer" not in st.session_state:
    st.session_state.answer = ""

if search:
    st.session_state.answer = ""
    with st.spinner("Jarvis is thinking..."):
        time.sleep(0.6)
        q = search.lower()
        if "backup" in q:
            st.session_state.answer = "🔐 <b>Follow KB7709271, step 7.1 section B.</b>"
        elif "cpu" in q:
            st.session_state.answer = "💡 Check running processes, consider scaling resources."
        elif "login" in q:
            st.session_state.answer = "🔎 Investigate authentication logs and reset as needed."
        else:
            st.session_state.answer = "🤖 I'm Jarvis. Ask me about incidents, cloud status, or best practices!"

if st.session_state.answer:
    st.markdown(
        f'<div class="ai-answer-bubble">{st.session_state.answer}</div>',
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="footer-glass">'
    "Minimal, premium Jarvis UI &bull; Powered by Streamlit • v0.1"
    '</div>',
    unsafe_allow_html=True
)
