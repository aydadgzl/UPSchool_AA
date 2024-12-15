import streamlit as st
import google.generativeai as genai
import pyttsx3
GeminiKey = "AIzaSyDzHW4PmZOFvyWb1J10yQi5kfqnZzlCVMM"
genai.configure(api_key=GeminiKey)
model = genai.GenerativeModel("gemini-1.5-flash")
def storyTime(age, issue, subject):
    prompt = f"""
    Let's write a fairy tale for a child whose information is given below, specific to the subject he experienced that day, his age and personality. It must be an educational tale / story on the specified subject!
    Information:
    Age: {age}
    Subject: {issue}
    Personal Feature: {subject}
    """
    response = model.generate_content(prompt)
    return response.text
st.title("Story Time")
st.write("What would you like to listen to today?")

age = st.number_input("Enter your age:", min_value=1, max_value=100, value=7)
issue = st.text_input("Enter the subject (e.g. sharing, learning):")
subject = st.text_input("Enter personal characteristic (e.g. patient, brave):")

if st.button("Write "):
    if issue and subject:
        masal = storyTime(age, issue, subject)

        st.subheader("Your story")
        st.write(masal)

        engine = pyttsx3.init()
        engine.save_to_file(masal, "masal.mp3")  # Save the spoken story to a file

        st.audio("masal.mp3", format="audio/mp3")

    else:
        st.warning("Please make sure you fill in all the information.")
