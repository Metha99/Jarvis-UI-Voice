import streamlit as st
import time

st.set_page_config(page_title="Jarvis AI", page_icon="🤖", layout="wide")
st.title("Jarvis")

search = st.text_input("Ask Jarvis anything...", key="search_input")

if "answer" not in st.session_state:
    st.session_state.answer = ""

if search:
    st.session_state.answer = ""
    with st.spinner("Jarvis is thinking..."):
        time.sleep(0.8)
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
        f'<div style="max-width:650px;margin:32px auto 0 auto;background:rgba(60,55,90,0.76);'
        'color:#dad9fa;border-radius:15px;box-shadow:0 2px 16px #2a295766;font-size:1.15em;'
        'padding:1.3em 1.6em;">'
        f'{st.session_state.answer}</div>',
        unsafe_allow_html=True
    )

st.caption("Professional, minimal Jarvis demo • Streamlit • v0.1")
