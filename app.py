import streamlit as st

st.set_page_config(page_title="Simple Python Web Page", page_icon="🌐")

st.title("Welcome")
st.write("This is a simple web page created using Python.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! Welcome to the webpage.")
    else:
        st.warning("Please enter your name.")