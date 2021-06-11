import cv2 as cv
#import numpy as np

cap = cv.VideoCapture('/home/user/Downloads/GOW 3.avi')


if cap.isOpened() == False:
    print("Error opening video stream or file")


frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        out.write(frame)

        cv.imshow('frame', frame)

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

    else:
        break


cap.release()
out.release()
cv.destroyAllWindows()
