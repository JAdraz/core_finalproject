import streamlit as st
from data_manipulation import test
import cv2 

# Title
st.set_page_config("Recognition", layout="centered")

# Header
st.title("Are you Jesus or Obama :male-detective:")

# Body
with st.container():
    col1, col2, col3 = st.columns(3)
    var1 = col1.button("Open Camera")
    col2.button("Stop Camera")
    if col3.button("Back to main"):
        url = "http://localhost:8501/"
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{url}\'" />', unsafe_allow_html=True)

a = test.cut_frame()

if var1:
    # Start camera
    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)
    n = 5*24
    st.write("Verifying in 5 seconds.")
    st.write("Please place yourself in front of the camera.")
    while n > 0:
        ret, raw_frame = cap.read()
        video_capture = a(raw_frame)                
        FRAME_WINDOW.image(video_capture)
        n -= 1
         # if n%24 == 0:
         #     st.write(n/24+1)
        # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

known_face_encodings, known_face_names = test.face_training()
face_locations, face_encodings, face_names, frame = test.transformarImagenes()
var2 = test.mostrarResultados()