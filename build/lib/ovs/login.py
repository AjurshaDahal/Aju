import cv2
import face_recognition
import numpy as np
from .db_connection import connect_db
from .voting import vote_for_party

def start_video_capture(voter_id):
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Please position your face within the frame to log in.")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not capture image from webcam.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

        cv2.imshow("Login Face", frame)

        if len(face_locations) > 0:
            login_face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            try:
                connection = connect_db()
                if connection:
                    cursor = connection.cursor()
                    cursor.execute("SELECT face_encoding FROM voters WHERE voter_id = %s", (voter_id,))
                    result = cursor.fetchone()

                    if result:
                        db_face_encoding = np.frombuffer(result[0], dtype=np.float64)
                        matches = face_recognition.compare_faces([db_face_encoding], login_face_encodings[0])

                        if matches[0]:
                            print("Login Successful!")
                            vote_for_party(voter_id)
                            video_capture.release()
                            cv2.destroyAllWindows()
                            return
                        else:
                            print("Face did not match. Login failed.")
                    else:
                        print("Voter ID not found in the database.")

                    cursor.close()
                    connection.close()
            except Exception as e:
                print(f"Database error: {e}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting login process.")
            break

    video_capture.release()
    cv2.destroyAllWindows()
