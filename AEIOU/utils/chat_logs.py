import streamlit as st


def Show_chat_logs():
    if st.session_state.memory:
        for item in st.session_state.memory:
            st.chat_message(name=item["role"]).write(item["content"])
