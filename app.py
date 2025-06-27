import streamlit as st
import time

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="centered")

# Apple-style: crisp white, minimal blue, premium feel
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: #f7faff !important;
    }
    .jarvis-orb {
        margin: 0 auto 12px auto;
        width: 48px; height: 48px; border-radius: 50%;
        background: radial-gradient(circle at 60% 40%, #e3e9ff 0%, #489aff 60%, #232366 100%);
        box-shadow: 0 0 16px #9cc3ff77;
        display: block;
    }
    .jarvis-header {
        text-align:center;
        font-size: 2.1em;
        font-weight: 700;
        font-family: 'Inter',sans-serif;
        color: #2b3c56;
        letter-spacing: 1.5px;
        margin-bottom: 0.17em;
    }
    .welcome-desc {
        text-align: center;
        color: #9da8be;
        font-size: 1.11em;
        margin-bottom: 1.4em;
        font-family: 'Inter',sans-serif;
    }
    .chat-panel {
        background: #fff;
        max-width: 480px;
        min-width: 340px;
        margin: 32px auto 0 auto;
        border-radius: 22px;
        box-shadow: 0 8px 32px #e2ebff42, 0 1.5px 6px #bbcdf616;
        padding: 2.2em 1.3em 1.7em 1.3em;
        display: flex; flex-direction: column;
        min-height: 440px;
    }
    .bubble-ai, .bubble-user {
        margin: 0.21em 0 1.0em 0;
        padding: 1.02em 1.21em;
        border-radius: 17px;
        font-family: 'Inter', sans-serif;
        font-size: 1.09em;
        line-height: 1.6;
        display: inline-block;
        max-width: 84%;
        word-break: break-word;
    }
    .bubble-ai {
        background: #f3f7fc;
        color: #2e3a56;
        border-bottom-left-radius: 7px;
        margin-right: auto;
    }
    .bubble-user {
        background: #489aff;
        color: #fff;
        border-bottom-right-radius: 7px;
        margin-left: auto;
        box-shadow: 0 1.5px 12px #81c3fd21;
    }
    .chat-input-row {
        display: flex;
        align-items: center;
        gap: 0.8em;
        margin-top: 1.5em;
    }
    .chat-inp {
        flex: 1;
        border: none;
        outline: none;
        background: #f5f7fb;
        font-size: 1.12em;
        padding: 0.93em 1.13em;
        border-radius: 13px;
        font-family: 'Inter',sans-serif;
        color: #1c263d;
        box-shadow: 0 1px 5px #bdd5ff0e;
        margin-right: 0.2em;
    }
    .send-btn {
        border: none;
        background: #489aff;
        border-radius: 50%;
        width: 41px; height: 41px;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer;
        transition: background 0.19s;
    }
    .send-btn:hover { background: #236cc9; }
    .send-icon { color: #fff; font-size: 1.25em; }
    </style>
    <link href="https://fonts.googleapis.com/css?family=Inter:600,800" rel="stylesheet">
""", unsafe_allow_html=True)

# Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome area
st.markdown('<div class="jarvis-orb"></div>', unsafe_allow_html=True)
st.markdown('<div class="jarvis-header">Jarvis</div>', unsafe_allow_html=True)
st.markdown('<div class="welcome-desc">Minimal, premium AI assistant. Ask anything about incidents, cloud, or best practice.</div>', unsafe_allow_html=True)

st.markdown('<div class="chat-panel">', unsafe_allow_html=True)
# Display Chat History
for msg in st.session_state.messages:
    bubble = "bubble-ai" if msg["role"] == "ai" else "bubble-user"
    st.markdown(f'<div class="{bubble}">{msg["content"]}</div>', unsafe_allow_html=True)

# Input row
with st.form(key="chat_form", clear_on_submit=True):
    cols = st.columns([8, 1])
    user_input = cols[0].text_input("", placeholder="Type your message and press Enter...", key="input_text")
    send = cols[1].form_submit_button("➤")
    st.markdown("<style>div.row-widget.stButton {display:none;}</style>", unsafe_allow_html=True)

if send and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Jarvis is thinking..."):
        time.sleep(0.6)
        m = user_input.lower()
        if "backup" in m:
            ai_text = "🔐 Follow KB7709271, step 7.1 section B."
        elif "cpu" in m:
            ai_text = "💡 Check running processes, consider scaling resources."
        elif "login" in m:
            ai_text = "🔎 Investigate authentication logs and reset as needed."
        else:
            ai_text = "🤖 I'm Jarvis. How can I help you today?"
        st.session_state.messages.append({"role": "ai", "content": ai_text})
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown(
    "<div style='margin-top:42px;color:#a4acc9;text-align:center;font-size:0.97em;'>Minimal, premium Jarvis UI • Powered by Streamlit • v0.1</div>",
    unsafe_allow_html=True
)
