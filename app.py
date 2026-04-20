
import streamlit as st
from datetime import datetime
import time

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

# Theme Selection
st.sidebar.subheader("🎨 Theme")
theme = st.sidebar.selectbox("Choose Theme", ["Light", "Dark", "Blue"])
st.sidebar.write(f"Selected Theme: {theme}")

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

    city = st.text_input("Enter your city")
    favorite_color = st.color_picker("Pick your favorite color")
    birth_date = st.date_input("Select your birth date")

    # Feedback Section
    rating = st.slider("Rate this webpage", 1, 10, 5)
    feedback = st.text_area("Write your feedback")

    # File Upload
    uploaded_file = st.file_uploader("Upload a profile picture", type=["jpg", "png", "jpeg"])

    # Checkbox
    agree = st.checkbox("I agree to share my details")

    # Submit Button
    if st.button("Submit"):
        if name and agree:
            with st.spinner("Submitting your details..."):
                time.sleep(2)

            st.success(f"Hello, {name}! Welcome to the webpage.")
            st.balloons()

            st.subheader("👤 User Details")
            st.write("Name:", name)
            st.write("Age:", age)
            st.write("Gender:", gender)
            st.write("City:", city)
            st.write("Birth Date:", birth_date)
            st.write("Favorite Color:", favorite_color)
            st.write("Hobbies:", ", ".join(hobby) if hobby else "No hobbies selected")
            st.write("Login Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

            if uploaded_file is not None:
                st.image(uploaded_file, caption="Uploaded Profile Picture", width=150)

            st.subheader("📌 Activity Status")
            st.info(f"{name} accessed the webpage successfully.")

            st.subheader("⭐ Feedback")
            st.write(f"You rated this webpage: {rating}/10")
            st.write("Your Feedback:", feedback if feedback else "No feedback given")

            # Progress Bar
            st.subheader("📊 Profile Completion")
            progress = 0
            if name:
                progress += 15
            if age:
                progress += 15
            if gender:
                progress += 15
            if hobby:
                progress += 15
            if city:
                progress += 10
            if favorite_color:
                progress += 10
            if feedback:
                progress += 10
            if uploaded_file:
                progress += 10

            st.progress(progress)
            st.write(f"Profile Completion: {progress}%")

            # Display Current Date and Time
            st.subheader("🕒 Current Date and Time")
            st.write(datetime.now().strftime("%A, %d %B %Y - %I:%M:%S %p"))

            # Metric Section
            st.subheader("📈 Quick Stats")
            col1, col2, col3 = st.columns(3)
            col1.metric("Age", age)
            col2.metric("Rating", rating)
            col3.metric("Hobbies Selected", len(hobby))

        else:
            st.warning("Please enter your name and agree to share your details.")

# About Page
elif page == "About":
    st.header("ℹ️ About")
    st.write("This webpage is built using Streamlit and Python.")
    st.write("It collects user details and displays information dynamically.")

    st.subheader("🚀 Features")
    st.write("- User Registration Form")
    st.write("- Profile Completion Tracker")
    st.write("- Feedback and Rating System")
    st.write("- File Upload Feature")
    st.write("- Dynamic Date and Time")

# Contact Page
elif page == "Contact":
    st.header("📞 Contact")
    st.write("Email: example@gmail.com")
    st.write("Phone: +91 9876543210")
    st.write("Address: Mumbai, India")

    contact_message = st.text_area("Send us a message")
    if st.button("Send Message"):
        st.success("Your message has been sent successfully!")

# Footer
st.markdown("---")
st.caption("Created using Python and Streamlit")

