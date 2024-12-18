import streamlit as st
from agents.workflow import ChaeUm
from utils.setting import Setting
from utils.chat_logs import Show_chat_logs
from utils.input_box import Main_input_box


def Sidebar():
    with st.sidebar:
        st.write("i'm sidebar")


def main():

    emptyLeft, mainPart, emptyRight = st.columns([1, 10, 1])
    with mainPart:
        Show_chat_logs()
        Main_input_box()
        if st.session_state.user_input_instance:
            human_input = {
                "role": "human",
                "content": st.session_state.user_input_instance,
            }
            st.session_state.memory.append(human_input)
            agent_output = {
                "role": "ai",
                "content": ChaeUm.invoke({"messages": st.session_state.memory})[
                    "messages"
                ][-1].content,
            }
            st.session_state.memory.append(agent_output)
            st.session_state.user_input_instance = ""
            st.rerun()


if __name__ == "__main__":
    Setting()
    Sidebar()
    main()
