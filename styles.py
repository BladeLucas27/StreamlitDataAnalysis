import streamlit as st

def css(path: str = "css/global.css", inline: str | None = None) -> None:
    if inline is not None:
        st.markdown(f"<style>{inline}</style>", unsafe_allow_html=True)
        return

    with open(path, "r") as fp:
        st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)