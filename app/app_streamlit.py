# app/streamlit_app.py
import streamlit as st

st.title("ICU Early Warning — Test")
st.write("If you see this, Streamlit is working.")

if st.button("Say hi"):
    st.write("Hello! Streamlit is ready.")
