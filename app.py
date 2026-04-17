
import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Simple Python Web Page",
    page_icon="🌐",
    layout="centered"
)

# Title Section
st.title("🌐 Welcome to the Python Web Page")
st.write("This is a simple web page created using Python and Streamlit.")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About", "Contact"]
)

# Home Page
if page == "Home":
    st.header("🏠 Home Page")

    # User Input
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    hobby = st.multiselect(
        "Select your hobbies",
        ["Reading", "Music", "Sports", "Coding", "Traveling"]
    )

    # Feedback Section
    rating = st.slider("Rate this webpage", 1, 10, 5)

    # Submit Button
    if st.button("Submit"):
        if name:
            st.success(f"Hello, {name}! Welcome to the webpage.")

            st.subheader("👤 User Details")
            st.write("Name:", name)
            st.write("Age:", age)
            st.write("Gender:", gender)
            st.write("Hobbies:", ", ".join(hobby) if hobby else "No hobbies selected")
            st.write("Login Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

            st.subheader("📌 Activity Status")
            st.info(f"{name} accessed the webpage successfully.")

            st.subheader("⭐ Feedback")
            st.write(f"You rated this webpage: {rating}/10")

            # Progress Bar
            st.subheader("📊 Profile Completion")
            progress = 0
            if name:
                progress += 25
            if age:
                progress += 25
            if gender:
                progress += 25
            if hobby:
                progress += 25

            st.progress(progress)
            st.write(f"Profile Completion: {progress}%")

            # Display Current Date and Time
            st.subheader("🕒 Current Date and Time")
            st.write(datetime.now().strftime("%A, %d %B %Y - %I:%M:%S %p"))

        else:
            st.warning("Please enter your name.")

# About Page
elif page == "About":
    st.header("ℹ️ About")
    st.write("This webpage is built using Streamlit and Python.")
    st.write("It collects user details and displays information dynamically.")

# Contact Page
elif page == "Contact":
    st.header("📞 Contact")
    st.write("Email: example@gmail.com")
    st.write("Phone: +91 9876543210")

# Footer
st.markdown("---")
st.caption("Created using Python and Streamlit")