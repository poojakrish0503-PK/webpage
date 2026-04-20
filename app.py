import streamlit as st
from datetime import datetime
import time
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Simple Python Web Page",
    page_icon="🌐",
    layout="centered"
)

# Session State for Login + Data Storage
if "submitted_data" not in st.session_state:
    st.session_state.submitted_data = []

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Title
st.title("🌐 Welcome to the Python Web Page")
st.write("Enhanced Streamlit Web App with Extra Features")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Dashboard"])

st.sidebar.subheader("🎨 Theme")
theme = st.sidebar.selectbox("Choose Theme", ["Light", "Dark", "Blue"])

# ---------------- LOGIN SIMULATION ----------------
st.sidebar.subheader("🔐 Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    if username and password:
        st.session_state.logged_in = True
        st.sidebar.success("Logged in successfully!")
    else:
        st.sidebar.warning("Enter credentials")

# ---------------- HOME PAGE ----------------
if page == "Home":

    if not st.session_state.logged_in:
        st.warning("Please login from sidebar first!")
    else:
        st.header("🏠 Home Page")

        name = st.text_input("Enter your name")
        email = st.text_input("Enter your email")

        age = st.number_input("Enter your age", 1, 100)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        hobby = st.multiselect("Hobbies", ["Reading", "Music", "Sports", "Coding", "Traveling"])
        city = st.text_input("City")

        favorite_color = st.color_picker("Favorite Color")
        birth_date = st.date_input("Birth Date")

        rating = st.slider("Rate this webpage", 1, 10, 5)
        feedback = st.text_area("Feedback")

        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

        agree = st.checkbox("I agree to share details")

        # Clear button
        clear = st.button("Clear Form")
        if clear:
            st.experimental_rerun()

        # Submit
        if st.button("Submit"):
            if name and email and agree:

                with st.spinner("Submitting..."):
                    time.sleep(1.5)

                data = {
                    "Name": name,
                    "Email": email,
                    "Age": age,
                    "Gender": gender,
                    "City": city,
                    "Hobbies": ", ".join(hobby),
                    "Rating": rating,
                    "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                st.session_state.submitted_data.append(data)

                st.success(f"Welcome {name}!")
                st.balloons()

                st.image(uploaded_file, width=150) if uploaded_file else None

                st.write("### Profile Summary")
                st.json(data)

            else:
                st.warning("Fill name, email and agree checkbox")

# ---------------- ABOUT PAGE ----------------
elif page == "About":
    st.header("ℹ️ About")
    st.write("Streamlit multi-feature web application")
    st.write("Includes login, analytics, and data storage")

# ---------------- CONTACT PAGE ----------------
elif page == "Contact":
    st.header("📞 Contact")
    msg = st.text_area("Message")

    if st.button("Send"):
        st.success("Message sent successfully!")

# ---------------- DASHBOARD ----------------
elif page == "Dashboard":

    st.header("📊 Dashboard")

    if st.session_state.submitted_data:

        df = pd.DataFrame(st.session_state.submitted_data)
        st.dataframe(df)

        # Download CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Data", csv, "user_data.csv", "text/csv")

        # Hobby chart
        st.subheader("🎯 Hobby Analysis")

        hobby_counts = {}
        for row in st.session_state.submitted_data:
            for h in row["Hobbies"].split(", "):
                hobby_counts[h] = hobby_counts.get(h, 0) + 1

        chart_df = pd.DataFrame({
            "Hobby": list(hobby_counts.keys()),
            "Count": list(hobby_counts.values())
        })

        fig = px.bar(chart_df, x="Hobby", y="Count")
        st.plotly_chart(fig)

    else:
        st.info("No data available yet")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built using Python + Streamlit 🚀")