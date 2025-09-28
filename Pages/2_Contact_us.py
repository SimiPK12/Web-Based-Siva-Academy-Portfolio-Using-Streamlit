import streamlit as st


st.title(":blue[📩 Contact Us]")

st.write(
    "Have questions or need more information? Fill out the form below and our team will get back to you."
)

# Contact form
with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email", "example@abc.com")
    course = st.selectbox(
        "Which course are you interested in?",
        ["Python", "Data Science", "Machine Learning", "Deep Learning", "Full Stack Development"]
    )
    message = st.text_area("Your Query / Message")
    
    submitted = st.form_submit_button("📨 Send Enquiry")

    if submitted:
        st.success(f"✅ Thanks {name}! We’ve received your enquiry about **{course}**. Our team will contact you at {email}.")
        st.balloons()

# Extra info section
st.markdown("---")
st.subheader("📍 Our Office")
st.write("Siva Academy, Bangalore, India")

st.subheader("📞 Call Us")
st.write("+91-8951956502")

st.subheader("✉️ Email")
st.write("sivaacademy.net")
