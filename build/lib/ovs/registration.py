import cv2
import face_recognition
import numpy as np
from .db_connection import connect_db

def register_voter(voter_id):
    print(f"Attempting to register Voter ID: {voter_id}")
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not access the webcam.")
        return

    try:
        connection = connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM voters WHERE voter_id = %s", (voter_id,))
            result = cursor.fetchone()
            if result:
                print(f"Voter ID {voter_id} is already registered.")
                cursor.close()
                connection.close()
                video_capture.release()
                return
            cursor.close()
            connection.close()
    except Exception as e:
        print(f"Database error: {e}")
        video_capture.release()
        return

    print("Please position your face within the frame for registration.")
    face_registered = False

    while not face_registered:
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not capture image from webcam.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Register Face", frame)

        if len(face_locations) == 1:
            face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            print("Face detected. Registering...")
            try:
                connection = connect_db()
                if connection:
                    cursor = connection.cursor()
                    face_encoding_bytes = face_encoding.tobytes()
                    cursor.execute(
                        "INSERT INTO voters (voter_id, face_encoding) VALUES (%s, %s)",
                        (voter_id, face_encoding_bytes),
                    )
                    connection.commit()
                    print(f"Voter ID {voter_id} registered successfully.")
                    face_registered = True
                    cursor.close()
                    connection.close()
            except Exception as e:
                print(f"Database error: {e}")
                break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting registration process.")
            break

    video_capture.release()
    cv2.destroyAllWindows()
