import streamlit as st
# from data_manipulation.test import cut_frame, face_training, transformarImagenes, mostrarResultados
import cv2
import face_recognition

# Title
st.set_page_config("Recognition", layout="centered")

# Header
st.title("Who are you? :male-detective:")

# Body
with st.container():
    col1, col2, col3 = st.columns(3)
    var1 = col1.button("Open Camera")
    if col2.button("Stop Camera"):
        var1 = False
    if col3.button("Back to main"):
        url = "http://localhost:8501/"
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{url}\'" />', unsafe_allow_html=True)


jesus_image_path = "data/train/Jesus/IMG_3462.jpg"
obama_image_path = "data/train/Obama/Obama006.jpg"

# Load a sample picture and learn how to recognize it.
jesus_image = face_recognition.load_image_file(jesus_image_path)
jesus_face_encoding = face_recognition.face_encodings(jesus_image)[0]

# Load a second sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file(obama_image_path)
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Create list of known face encodings and their names
known_face_encodings = [jesus_face_encoding, obama_face_encoding]
known_face_names = ["Jesus Adraz", "Barak Obama"]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while var1:
    ret, frame = camera.read()
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        # rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
        
            face_names.append(name)

        # process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        # cv2.imshow('Video', frame)
      
        # Hit 'q' on the keyboard to quit!
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

        FRAME_WINDOW.image(result)
camera.release()
cv2.destroyAllWindows()


# if var1:
#     # Start camera
#     FRAME_WINDOW = st.image([])
#     cap = cv2.VideoCapture(1)
#     while var1:
#         ret, raw_frame = cap.read()
#         raw_frame = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2RGB)
#         FRAME_WINDOW.image(raw_frame)
#     # Release the webcam
#     cap.release()
#     cv2.destroyAllWindows()