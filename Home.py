import streamlit as st

from PIL import Image
st.title("WELCOME TO :blue[SIVA ACADEMY]")




col1,col2 = st.columns(2)

with col1:

    IMG_PATH = "C:\\Users\\bhagy\\OneDrive\\Desktop\\Streamlit_proj\\Proj3\\Resources\\Images\\logo.png"
    image = Image.open(IMG_PATH)

    st.image(image, use_container_width=True)

with col2:
    st.subheader("Company name : Siva Academy ")

    st.subheader("Location : Bangalore")

    st.subheader("Since 2023")

basic_description = """At Siva Academy, we offer comprehensive, hands-on training programs designed to prepare you for real-world IT careers. Whether you're a beginner looking to start your journey in tech or a professional aiming to upskill, our experienced instructors and industry-aligned curriculum will help you succeed."""

st.write(basic_description)
