import streamlit as st


def Setting():
    st.set_page_config(
        page_title="AEIOU",
        layout="wide",
    )

    if not st.session_state.memory:
        st.session_state.memory = [{"role": "ai", "content": "안녕하세요! 반갑습니다."}]
    if not st.session_state.user_input_instance:
        st.session_state.user_input_instance = ""

    st.title(
        body="AEIOU demo",
    )
