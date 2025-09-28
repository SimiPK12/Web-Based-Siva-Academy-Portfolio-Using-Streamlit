import streamlit as st

st.title(" :red[Services offered]")




st.header("Courses Offered")
with st.expander("Data Science Course"):
    st.write("Duration : 6 months")
    st.write("Modules : Python,Data Analysis,ML,DL")
    st.write("fees: 70000 INR")

with st.expander("Full stack Java course"):
    st.write("Duration : 6 months")
    st.write("Modules : Frontend,backend")
    st.write("fees: 60000 INR")




col1, col2 = st.columns(2)

with col1:
    st.header(":blue[WHY SIVA ACADEMY?]")
    with open(r"C:\Users\bhagy\OneDrive\Desktop\Streamlit_proj\Proj3\Resources\Video\Welcome_video.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes)

with col2:
    st.subheader("Enquire About Course")
    email = st.text_input("Enter your email", placeholder="example@abc.com")

    course = st.selectbox(
        "Which course are you interested in?",
        ["Python", "Data Science", "Machine Learning", "Deep Learning", "Full Stack Development"]
    )

    query = st.text_area("Enter your query / message")

    btn_click = st.button("Submit")

    if btn_click:
        st.success(f"Thanks {email}! We’ll get back to you about **{course}** soon.")
        st.balloons()
