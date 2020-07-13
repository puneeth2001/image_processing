import cv2
import numpy as np

cap = cv2.VideoCapture(2)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# outfile = cv2.VideoWriter('output.avi', fourcc, 20.0,(640,480))

while True:
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # outfile.write(frame)
    cv2.imshow('frame',frame)
    # cv2.imshow('grey',grey)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
