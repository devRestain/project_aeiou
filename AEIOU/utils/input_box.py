import streamlit as st


def Main_input_box():
    def Submit():
        if st.session_state.widget == "":
            return
        st.session_state.user_input_instance = st.session_state.widget
        st.session_state.widget = ""

    st.text_input(
        label="여기에 입력하세요!",
        key="widget",
        on_change=Submit,
    )
