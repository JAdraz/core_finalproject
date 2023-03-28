import streamlit as st

# Title
st.set_page_config("Recognition", layout="centered")

# Header
st.title("Are you Jesus or Obama :male-detective:")

# Body
with st.container():
    col1, col2, col3 = st.columns(3)
    col1.button("Open Camera")
    col2.button("Stop Camera")
    if col3.button("Back to main"):
        url = "http://localhost:8501/"
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{url}\'" />', unsafe_allow_html=True)