import streamlit as st
import time

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: #161821 !important;
    }
    .jarvis-core {
        margin-top: 56px;
        margin-bottom: 16px;
        display: flex; flex-direction: column; align-items: center;
    }
    .jarvis-orb {
        width: 98px; height: 98px; border-radius: 50%;
        background: radial-gradient(circle at 60% 40%, #d0d7ff 0%, #5566ff 60%, #262b41 100%);
        box-shadow: 0 0 48px 16px #4747e7cc, 0 0 0 22px #1d2042a8;
        animation: orbPulse 3s infinite alternate;
        margin-bottom: 18px;
        transition: box-shadow 0.5s;
    }
    @keyframes orbPulse {
        from { box-shadow: 0 0 48px 8px #5555ffa0, 0 0 0 10px #202146b8;}
        to { box-shadow: 0 0 80px 36px #b5aaf9b0, 0 0 0 28px #343a7ca0;}
    }
    .jarvis-title {
        font-size: 2.9em; font-family: 'Orbitron', 'Montserrat', sans-serif;
        font-weight: 900; letter-spacing: 4px; word-spacing: 3px;
        background: linear-gradient(97deg,#ccd3fd,#4669ff 50%,#3841b9 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 2.2em; margin-top: 0;
    }
    .input-outer {
        width: 100vw; display: flex; flex-direction: column; align-items: center;
    }
    .glass-search {
        width: 100%;
        max-width: 710px;
        background: rgba(32,36,54,0.90);
        border-radius: 16px;
        box-shadow: 0 3px 40px 0 #3b366680, 0 1px 1px #222;
        border: 1.8px solid #232464;
        padding: 1.3em 1.7em 1.3em 1.8em;
        font-size: 1.17em;
        color: #ececff;
        margin-bottom: 28px;
        font-family: 'Montserrat', 'Orbitron', sans-serif;
        outline: none;
        transition: border 0.25s, box-shadow 0.25s;
    }
    .glass-search:focus {
        border: 2.5px solid #7581ff;
        box-shadow: 0 0 10px 2px #6674fa66;
        background: rgba(38,48,84,0.98);
    }
    .ai-bubble-premium {
        max-width: 670px;
        margin: 42px auto 0 auto;
        background: linear-gradient(107deg,rgba(60,62,100,0.78) 55%,rgba(90,90,152,0.43) 100%);
        color: #e6e7fa;
        border-radius: 18px;
        box-shadow: 0 2px 32px #35357366;
        font-size: 1.25em;
        font-family: 'Montserrat', sans-serif;
        padding: 1.4em 1.7em;
        animation: fadeIn 1.25s;
        border: 1.2px solid #4657ff5c;
    }
    @keyframes fadeIn {
        0% {opacity:0; transform:scale(0.97);}
        100% {opacity:1; transform:scale(1);}
    }
    .footer-premium {
        margin-top: 88px; color: #7a7cf8a8; font-size: 1.04em; text-align:center;
        letter-spacing: 1.5px; font-family: 'Montserrat',sans-serif;
    }
    </style>
    <link href="https://fonts.googleapis.com/css?family=Orbitron:600|Montserrat:400,700" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(
    '<div class="jarvis-core">'
    '<div class="jarvis-orb"></div>'
    '<div class="jarvis-title">Jarvis</div>'
    '</div>', unsafe_allow_html=True
)

st.markdown('<div class="input-outer">', unsafe_allow_html=True)

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
        time.sleep(0.85)
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
        f'<div class="ai-bubble-premium">{st.session_state.answer}</div>',
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="footer-premium">'
    "Minimal, premium Jarvis UI &bull; Powered by Streamlit &bull; v0.1"
    '</div>',
    unsafe_allow_html=True
)
