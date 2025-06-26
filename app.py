import streamlit as st

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")

st.markdown(
    """
    <style>
        .jarvis-header {font-size:2.7em;font-weight:bold;color:#6E44FF;margin-bottom:1.3em;}
        .ai-bubble {background:#29283b;color:#e1e0f5;border-radius:14px;padding:1.3em 1.5em;margin:1em auto;max-width:650px;}
        .center {display:flex;flex-direction:column;align-items:center;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="center"><div class="jarvis-header">Jarvis</div></div>', unsafe_allow_html=True)

search = st.text_input("", placeholder="Ask Jarvis anything...")

if search:
    st.markdown(f'<div class="ai-bubble">🔐 Example response for: "{search}"</div>', unsafe_allow_html=True)

st.caption("Minimal Jarvis demo • Streamlit • v0.1")
