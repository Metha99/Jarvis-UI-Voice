import streamlit as st
import time

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="centered")

# -------- GOOGLE-STYLE MODERN CHAT UI CSS --------
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: #f6f8fb !important;
    }
    .chat-container {
        max-width: 540px;
        margin: 64px auto 0 auto;
        background: #fff;
        border-radius: 24px;
        box-shadow: 0 4px 24px #dde2f8d9;
        padding: 2.4em 1.3em 2.2em 1.3em;
        min-height: 620px;
        display: flex; flex-direction: column;
        justify-content: flex-end;
    }
    .welcome-section {
        text-align: center;
        margin-bottom: 1.4em;
    }
    .ai-orb {
        margin-bottom: 0.4em;
        width: 58px; height: 58px; border-radius: 50%;
        background: radial-gradient(circle at 60% 40%, #e0e8fe 0%, #387cf7 65%, #232366 100%);
        box-shadow: 0 0 18px 0 #5b97ff8a, 0 0 0 6px #dde2f866;
        display: inline-block;
    }
    .welcome-title {
        font-size: 2em;
        font-family: 'Inter', sans-serif;
        color: #1c2c4c;
        font-weight: 800;
        margin-bottom: 0.22em;
    }
    .welcome-desc {
        color: #7485a8; font-size: 1.1em;
        font-family: 'Inter', sans-serif;
        letter-spacing: 1.1px;
        margin-bottom: 0.9em;
    }
    .chat-bubble-ai, .chat-bubble-user {
        margin: 0.28em 0 0.8em 0;
        padding: 1.07em 1.3em;
        border-radius: 18px;
        font-family: 'Inter', sans-serif;
        font-size: 1.11em;
        line-height: 1.65;
        display: inline-block;
        max-width: 90%;
        box-shadow: 0 1.5px 16px #c3cef61a;
    }
    .chat-bubble-ai {
        background: #f3f6fb;
        color: #23294e;
        border-bottom-left-radius: 6px;
        margin-right: auto;
    }
    .chat-bubble-user {
        background: #387cf7;
        color: #fff;
        border-bottom-right-radius: 6px;
        margin-left: auto;
        box-shadow: 0 1.5px 12px #94b7ff21;
    }
    .chat-input-bar {
        margin-top: 1.3em;
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 12px #bfd2fa33;
        padding: 0.6em 1.1em 0.6em 1.1em;
        display: flex;
        align-items: center;
        gap: 0.7em;
    }
    .chat-input {
        border: none;
        outline: none;
        background: none;
        width: 95%;
        font-size: 1.09em;
        font-family: 'Inter', sans-serif;
        color: #23294e;
        padding: 0.5em 0;
    }
    .send-btn {
        border: none;
        background: #387cf7;
        border-radius: 50%;
        width: 42px; height: 42px;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer;
        box-shadow: 0 2px 8px #98baff22;
        transition: background 0.2s;
    }
    .send-btn:hover { background: #2260c8; }
    .send-icon { color: #fff; font-size: 1.35em; }
    </style>
    <link href="https://fonts.googleapis.com/css?family=Inter:600,800" rel="stylesheet">
""", unsafe_allow_html=True)

# ---- Session State for Chat ----
if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.markdown(
    '<div class="welcome-section">'
    '<div class="ai-orb"></div>'
    '<div class="welcome-title">Jarvis</div>'
    '<div class="welcome-desc">Your premium AI assistant. Ask about your cloud, code, or incidents.</div>'
    '</div>', unsafe_allow_html=True
)

# ---- Display Chat History ----
for msg in st.session_state.messages:
    bubble_class = "chat-bubble-ai" if msg["role"] == "ai" else "chat-bubble-user"
    st.markdown(f'<div class="{bubble_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# ---- Input Bar (workaround: Streamlit can't do real custom input, so fallback to st.text_input) ----
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Type your message and hit Enter...", key="input_text")
    submitted = st.form_submit_button("Send", help="Send message")
    # Hide the Streamlit button and use Enter only:
    st.markdown("<style>div.row-widget.stButton {display:none;}</style>", unsafe_allow_html=True)

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Simulate AI response (swap for LLM call)
    with st.spinner("Jarvis is thinking..."):
        time.sleep(0.85)
        msg = user_input.lower()
        if "backup" in msg:
            ai_text = "🔐 Follow KB7709271, step 7.1 section B."
        elif "cpu" in msg:
            ai_text = "💡 Check running processes, consider scaling resources."
        elif "login" in msg:
            ai_text = "🔎 Investigate authentication logs and reset as needed."
        else:
            ai_text = "🤖 I'm Jarvis. How can I help you today?"
        st.session_state.messages.append({"role": "ai", "content": ai_text})
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    "<div style='margin-top:48px;color:#b5bed6;text-align:center;'>Minimal, premium Jarvis UI • Powered by Streamlit • v0.1</div>",
    unsafe_allow_html=True
)
