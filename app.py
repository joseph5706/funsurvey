import streamlit as st
import time

st.set_page_config(
    page_title="2026 Fun Survey",
    page_icon="😂"
)

st.title("😂 2026 Fun Survey")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100)

city = st.text_input("City")
college = st.text_input("College")
course = st.text_input("Course")
hobbies = st.text_input("Hobbies")
food = st.text_input("Favorite Food")
job = st.text_input("Dream Job")
goal = st.text_input("Goal in 5 years")


excited = st.radio(
    "Are you excited to see your survey result?",
    ["Yes", "Absolutely!"]
)


if st.button("Submit"):

    if name:

        st.success("Analyzing responses...")

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)


        st.balloons()

        st.header("😂 GOTCHA!")

        st.write(
            f"Congratulations {name}! "
            "Your personality analysis is complete..."
        )

        st.warning(
            "No information was saved. "
            "This was just a fun prank 😆"
        )


        video_file = open("fun.mp4", "rb")
        video_bytes = video_file.read()

        st.video(video_bytes)
