import streamlit as st
from resume_matcher import load_resume, calculate_similarity
import os  

st.title("🧠 AI Resume Matcher")

uploaded_resume = st.file_uploader("Upload Resume (.pdf or .docx)")
job_description = st.text_area("Paste Job Description")

if uploaded_resume and job_description:
    file_extension = os.path.splitext(uploaded_resume.name)[-1]
    temp_filename = f"temp_resume{file_extension}"

    with open(temp_filename, "wb") as f:
        f.write(uploaded_resume.getbuffer())

    resume_text = load_resume(temp_filename)
    score = calculate_similarity(resume_text, job_description)

    st.success(f"Resume Match Score: {score}%")

    # ✅ Cleanup temp file safely here
    if os.path.exists(temp_filename):
        os.remove(temp_filename)
