# video_from_webcam.py

import cv2

cap = cv2.VideoCapture(0)  # Open the first camera connected to the computer.

while True:
    ret, frame = cap.read()  # Read an image from the frame.
    # frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)
    cv2.imshow('frame', frame)  # Show the image on the display.
    # Close the script when q is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera device and close the GUI.
cap.release()
cv2.destroyAllWindows()
