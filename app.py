import streamlit as st

st.set_page_config(page_title="Jarvis AI", page_icon=":robot_face:", layout="wide")

st.markdown("""
    <style>
    .jarvis-header {font-size:2.4em;font-weight:bold;color:#6E44FF;}
    .message-bubble {padding:1em;border-radius:15px;margin-bottom:0.5em;}
    .user-bubble {background:#D1E8E4;}
    .ai-bubble {background:#E7DFFF;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="jarvis-header">Jarvis</div>', unsafe_allow_html=True)
#st.image('assets/jarvis_logo.png', width=80)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    if msg['role'] == "user":
        st.markdown(f'<div class="message-bubble user-bubble"><b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message-bubble ai-bubble"><b>Jarvis:</b> {msg["content"]}</div>', unsafe_allow_html=True)

user_prompt = st.text_input("Type your question for Jarvis...", key="user_input", label_visibility="collapsed")

def jarvis_respond(prompt):
    if "backup" in prompt.lower():
        return "Follow the KB article KB7709271, step 7.1 section B."
    elif "cpu" in prompt.lower():
        return "Check running processes, consider scaling resources."
    else:
        return "I'm Jarvis. How can I assist you with cloud incidents or infrastructure queries?"

if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    ai_response = jarvis_respond(user_prompt)
    st.session_state.chat_history.append({"role": "jarvis", "content": ai_response})
    st.experimental_rerun()

st.caption("Professional, minimal Jarvis demo • Powered by Streamlit • v0.1")
