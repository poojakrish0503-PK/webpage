import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Simple Python Web Page", page_icon="🌐")

st.title("Welcome")
st.write("This is a simple web page created using Python.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! Welcome to the webpage.")

        st.subheader("User Details")
        st.write("Name:", name)
        st.write("Login Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        st.subheader("Activity")
        st.info(f"{name} accessed the webpage successfully.")

    else:
        st.warning("Please enter your name.")