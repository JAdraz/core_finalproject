import streamlit as st


# Title
st.set_page_config("Home", layout="centered")

# Header
st.title("Welcome to Face Recognition :camera:")
st.image('./img/cover.png')

# Body
st.text("To start with face recognition, clic the bottom down below!")

if st.button("Start"):
    url = "http://localhost:8501/recognition"
    st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{url}\'" />', unsafe_allow_html=True)

