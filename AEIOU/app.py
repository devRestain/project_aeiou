import streamlit as st

st.set_page_config(
    page_title="AEIOU",
    layout="wide",
)
st.title(
    body="AEIOU demo",
)

with st.sidebar:
    st.write("i'm sidebar")

emptyLeft, mainPart, emptyRight = st.columns([1, 8, 1])


def main():
    with emptyLeft:
        st.write("i'm left.")
    with emptyRight:
        st.write("i'm right.")
    with mainPart:
        st.write("HI!")
        st.text_input("Give me Sth!")
    # 유저가 제안된 행동 중 선택하면 유저 취향 따라서 예상 소요시간 계산 후 저장


if __name__ == "__main__":
    main()
