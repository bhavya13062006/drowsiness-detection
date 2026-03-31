import cv2

# Load cascades
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Frame-based detection
closed_frames = 0
closed_frames_threshold = 20   # increase/decrease as needed

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    eyes_found = 0

    for (x, y, w, h) in faces:
        # Draw face box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Only check upper part of face for eyes
        roi_gray = gray[y:y + h // 2, x:x + w]
        roi_color = frame[y:y + h // 2, x:x + w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=6,
            minSize=(25, 25)
        )

        eyes_found = len(eyes)

        for (ex, ey, ew, eh) in eyes[:2]:
            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (0, 255, 0),
                2
            )

        break  # only use first detected face

    # Logic
    if len(faces) == 0:
        closed_frames = 0
        cv2.putText(
            frame,
            "No Face Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )
    else:
        if eyes_found >= 1:
            closed_frames = 0
            cv2.putText(
                frame,
                "Eyes Open",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )
        else:
            closed_frames += 1
            cv2.putText(
                frame,
                "Eyes Closed",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"Closed Frames: {closed_frames}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

            if closed_frames >= closed_frames_threshold:
                cv2.putText(
                    frame,
                    "ALERT! DRIVER DROWSY!",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()