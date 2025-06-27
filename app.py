import streamlit as st
import time

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")

# ----------- MODERN GLASSMORPHISM STYLE -----------
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #17181c 40%, #e9ebf7 170%);
    }
    .glass-panel {
        margin: 60px auto 0 auto;
        background: rgba(255,255,255,0.13);
        border-radius: 24px;
        box-shadow: 0 8px 36px 0 #41404c18, 0 1.5px 4.5px #14143212;
        backdrop-filter: blur(10px);
        padding: 2.4em 2.2em 2em 2.2em;
        max-width: 540px;
        min-width: 350px;
        border: 1.7px solid #2e348c1f;
        transition: box-shadow 0.2s;
    }
    .glass-panel:hover {
        box-shadow: 0 8px 52px 0 #5959ff28, 0 1.5px 4.5px #1d2344a0;
        border: 1.7px solid #4644ff2a;
    }
    .jarvis-header {
        font-size: 2.6em;
        letter-spacing: 3px;
        font-family: 'Montserrat', 'Inter', sans-serif;
        background: linear-gradient(87deg,#4654ff 30%,#1bcbe1 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900;
        margin-bottom: 12px;
        text-align:center;
        text-shadow: 0 2px 32px #3c78c399;
    }
    .subtext {
        color: #565684; text-align:center; margin-bottom: 1.7em;
        font-family: 'Inter', sans-serif;
        font-size: 1.12em;
        letter-spacing: 1.5px;
    }
    .input-bar {
        width: 100%;
        font-size: 1.17em;
        padding: 1.1em 1.1em 1.1em 1.3em;
        border-radius: 13px;
        border: 1.5px solid #c9caff7a;
        outline: none;
        margin-bottom: 24px;
        background: rgba(230,233,252,0.92);
        color: #23243b;
        font-family: 'Montserrat', 'Inter', sans-serif;
        box-shadow: 0 2px 20px #b6b4fc0f;
        transition: border 0.2s, box-shadow 0.2s;
    }
    .input-bar:focus {
        border: 2px solid #6b7aff;
        background: #fff;
        box-shadow: 0 0 14px #aab2ff44;
    }
    .ai-answer-bubble {
        margin: 38px auto 0 auto;
        background: linear-gradient(95deg,#f5f7ff 55%,#e7eaf7 100%);
        color: #343465;
        border-radius: 15px;
        box-shadow: 0 2px 28px #4c50a733;
        font-size: 1.16em;
        font-family: 'Inter', 'Montserrat', sans-serif;
        padding: 1.35em 1.6em;
        animation: fadeIn 1.15s;
        border: 1.4px solid #b3bdff54;
    }
    @keyframes fadeIn {
        0% {opacity:0; transform:translateY(30px);}
        100% {opacity:1; transform:translateY(0);}
    }
    .footer-glass {
        margin-top: 70px;
        color: #7b84d4c5;
        font-size: 1em;
        text-align:center;
        font-family: 'Inter',sans-serif;
        letter-spacing: 1.5px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:800|Inter:400,700" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
st.markdown('<div class="jarvis-header">Jarvis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Your minimal, premium AI assistant</div>', unsafe_allow_html=True)

# Custom search bar
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
    "Minimal, premium Jarvis UI &bull; Powered by Streamlit &bull; v0.1"
    '</div>',
    unsafe_allow_html=True
)
