import face_recognition
import cv2

# This function return the video dimensions
def cut_frame(frame):
    dim = 500
    x_offset = 500
    y_offset = 300
    frame = frame[y_offset:y_offset+dim, x_offset:x_offset+dim, :]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame


def face_training():

    jesus_image_path = "./data/train/Jesus/IMG_3462.jpg"
    obama_image_path = "./data/train/Obama/Obama006.jpg"

    # Load a sample picture and learn how to recognize it.
    jesus_image = face_recognition.load_image_file(jesus_image_path)
    jesus_face_encoding = face_recognition.face_encodings(jesus_image)[0]

    # Load a second sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file(obama_image_path)
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Create list of known face encodings and their names
    known_face_encodings = [jesus_face_encoding, obama_face_encoding]
    known_face_names = ["Jesus Adraz", "Barak Obama"]

    return known_face_encodings, known_face_names
     
def transformarImagenes(known_face_encodings, known_face_names,frame):
   
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True


    while True:
        # Grab a single frame of video
        # ret, frame = video_capture.read()
        # Only process every other frame of video to save time
        if process_this_frame:
            # # Resize frame of video to 1/4 size for faster face recognition processing
            # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            # rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                
                #Or instead, use the known face with the smallest distance to the new face
                #face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                #best_match_index = np.argmin(face_distances)
                #if matches[best_match_index]:
                    #name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame
        return face_locations, face_encodings, face_names, frame

def mostrarResultados(face_locations, face_names, frame):

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
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        var2 = cv2.imshow('Video', frame)

        # Release handle to the webcam
        return var2