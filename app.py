import streamlit as st
import time

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")

# ---------- CUSTOM STYLES AND ANIMATIONS ----------
st.markdown("""
    <style>
    body {
        background-color: #161821;
    }
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 95vh;
    }
    .jarvis-orb {
        margin-bottom: 18px;
        width: 72px; height: 72px; border-radius: 50%;
        background: radial-gradient(circle at 60% 40%, #9fa3f7, #3522d4 70%, #232366 100%);
        box-shadow: 0 0 32px #6150e7, 0 0 0 12px #2a2957;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 32px #6e44ff, 0 0 0 12px #232366;}
        50% { box-shadow: 0 0 64px #b5aaf9, 0 0 0 22px #2a2957;}
        100% { box-shadow: 0 0 32px #6e44ff, 0 0 0 12px #232366;}
    }
    .jarvis-title {
        font-size: 2.7em; letter-spacing: 2px; font-family: 'Orbitron', sans-serif;
        background: linear-gradient(90deg,#a0a9f4,#6e44ff,#3522d4);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.7em; font-weight: bold;
    }
    .jarvis-search {
        width: 100%;
        max-width: 650px;
        background: rgba(25, 25, 45, 0.97);
        border-radius: 18px;
        box-shadow: 0 2px 32px #1b1a2b44;
        border: none;
        padding: 1.5em 1.5em 1.5em 2.2em;
        font-size: 1.3em;
        color: #ececff;
        outline: none;
        margin-bottom: 30px;
        animation: slideIn 0.8s;
    }
    @keyframes slideIn {
        0% {opacity:0; transform:translateY(30px);}
        100% {opacity:1; transform:translateY(0);}
    }
    .ai-answer-bubble {
        max-width: 650px;
        margin: 32px auto 0 auto;
        background: rgba(60,55,90,0.76);
        color: #dad9fa;
        border-radius: 15px;
        box-shadow: 0 2px 16px #2a295766;
        font-size: 1.15em;
        padding: 1.3em 1.6em;
        animation: fadeIn 1.2s;
    }
    @keyframes fadeIn {
        0% {opacity:0; transform:scale(0.98);}
        100% {opacity:1; transform:scale(1);}
    }
    </style>
    <link href="https://fonts.googleapis.com/css?family=Orbitron:600" rel="stylesheet">
""", unsafe_allow_html=True)

# ----------- MAIN LAYOUT ----------
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.markdown('<div class="jarvis-orb"></div>', unsafe_allow_html=True)
st.markdown('<div class="jarvis-title">Jarvis</div>', unsafe_allow_html=True)

# ------- SEARCH BAR WITH INSTANT SUBMIT -------
search = st.text_input(
    "",  # no label
    key="search_input",
    placeholder="Ask me anything about your cloud, incidents, or infrastructure...",
    label_visibility="collapsed",
)

st.markdown('</div>', unsafe_allow_html=True)  # End centered block

# ------- AI ANSWER SIMULATION / FADE IN -------
if "answer" not in st.session_state:
    st.session_state.answer = ""

if search:
    # Simulate minimal "AI" response (replace with your LLM call)
    st.session_state.answer = ""
    with st.spinner("Jarvis is thinking..."):
        time.sleep(0.7)  # Simulate response delay
        if "backup" in search.lower():
            st.session_state.answer = "🔐 <b>Follow KB7709271, step 7.1 section B.</b>"
        elif "cpu" in search.lower():
            st.session_state.answer = "💡 Check running processes, consider scaling resources."
        elif "login" in search.lower():
            st.session_state.answer = "🔎 Investigate authentication logs and reset as needed."
        else:
            st.session_state.answer = "🤖 I'm Jarvis. Ask me about incidents, cloud status, or best practices!"

if st.session_state.answer:
    st.markdown(
        f'<div class="ai-answer-bubble">{st.session_state.answer}</div>',
        unsafe_allow_html=True
    )

st.markdown("""
<div style="margin-top: 60px; color: #5a588a; font-size: 1em; text-align:center;">
  Professional, futuristic Jarvis UI &bull; Powered by Streamlit &bull; v0.2
</div>
""", unsafe_allow_html=True)
