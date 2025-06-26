import streamlit as st

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")

st.markdown('<h1 style="color:#6E44FF; font-family:Orbitron, sans-serif;">Jarvis</h1>', unsafe_allow_html=True)

search = st.text_input("Type your question for Jarvis...")

if search:
    st.write("You asked:", search)
    st.write("Jarvis would reply here.")

st.caption("Professional, minimal Jarvis demo • Powered by Streamlit • v0.1")
