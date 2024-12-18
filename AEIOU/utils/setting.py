import streamlit as st


def Setting():
    st.set_page_config(
        page_title="AEIOU",
        layout="wide",
    )

    if "memory" not in st.session_state:
        st.session_state.memory = [{"role": "ai", "content": "안녕하세요! 반갑습니다."}]
    if "user_input_instance" not in st.session_state:
        st.session_state.user_input_instance = ""

    st.title(
        body="AEIOU demo",
    )
