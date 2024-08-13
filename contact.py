import streamlit as st
from PIL import Image
from pathlib import Path

def app(st, current_dir, Image):
    # Directory of needed files
    resume_file = current_dir / "Resume" / "MyResume.pdf"
    profile_pic = current_dir / "Photos" / "profile-pic.png"
    Linkedin_pic = current_dir / "Photos" / "linkedin.png"
    Github_pic = current_dir / "Photos" / "github.png"
    Gmail_pic = current_dir / "Photos" / "gmail.png"

    # Picture and summary
    c1, c2 = st.columns([1, 2])
    profile_pic = Image.open(profile_pic)
    c1.image(profile_pic, width=300)  # Increased width from 150 to 300
    with c2:
        st.header('About Me')
        st.markdown("<p style='font-size:20px;'>My name is <b>Oluwadamilola Kolawole</b>, and I am currently pursuing a Master's degree in Data Science at the University of Salford. I have a strong focus on machine learning and statistics and am eager to enhance my skills through hands-on, cutting-edge projects. I am passionate about applying my knowledge to tackle global challenges and contribute to advancements in technology and innovation.</p>", unsafe_allow_html=True)  # Increased font size
        st.markdown("<p style='font-size:16px;'><i>August 2024</i></p>", unsafe_allow_html=True)  # Increased caption size
        
        # Download Resume
        with open(resume_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name='Oluwadamilola_Kolawole_Resume.pdf',
            mime="application/octet-stream",
        )
            
    st.write('#')
    # ___________________________ Links __________________
    Linkedin_pic = Image.open(Linkedin_pic)
    Github_pic = Image.open(Github_pic)
    Gmail_pic = Image.open(Gmail_pic)

    with st.container():
        st.write("Connect with me:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image(Linkedin_pic, width=50)
            st.markdown('<a href="https://www.linkedin.com/in/oluwadamilola-kolawole" target="_blank">LinkedIn</a>', unsafe_allow_html=True)
        
        with col2:
            st.image(Github_pic, width=50)
            st.markdown('<a href="https://github.com/OluwadamilolaK" target="_blank">GitHub</a>', unsafe_allow_html=True)
        
        with col3:
            st.image(Gmail_pic, width=50)
            st.markdown('<a href="mailto:oluwadamilolakolawole9@gmail.com" target="_blank">Gmail</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    current_dir = Path('.')
    app(st, current_dir, Image)
