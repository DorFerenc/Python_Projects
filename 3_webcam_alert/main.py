import cv2
import time

print(cv2.__version__)
print(cv2.__file__)
video = cv2.VideoCapture(2) # main camera
# video = cv2.VideoCapture(1) # second camera

while True:
    time.sleep(1)
    check, frame = video.read()
    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()