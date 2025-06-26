import streamlit as st
import time

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")

# ---------- CUSTOM STYLES AND ANIMATIONS ----------
st.markdown("""
    <style>
    .centered {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
    }
    .jarvis-orb {
        margin-bottom: 18px; width: 72px; height: 72px; border-radius: 50%;
        background: radial-gradient(circle at 60% 40%, #9fa3f7, #3522d4 70%, #232366 100%);
        box-shadow: 0 0 32px #6150e7, 0 0 0 12px #2a2957; animation: pulse 2s infinite;
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

# ----------- MAIN LAYOUT (always renders a visible header!) ----------
st.markdown('<div class="centered"><div class="jarvis-orb"></div><div class="jarvis-title">Jarvis</div></div>', unsafe_allow_html=True)

search = st.text_input("Ask Jarvis anything...", key="search_input")

if "answer" not in st.session_state:
    st.session_state.answer = ""

if search:
    st.session_state.answer = ""
    with st.spinner("Jarvis is thinking..."):
        time.sleep(0.8)
        # Simple logic for demo; swap in your LLM for production
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

st.caption("Professional, minimal Jarvis demo • Streamlit • v0.1")
