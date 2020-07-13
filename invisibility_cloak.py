import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(2)

time.sleep(3)

count = 0
background =0

for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    count+=1
    img = np.flip(img, axis=1)

    # convert color
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # generate masks to detect red color
    lower_red = np.array([0,125,50])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170,120, 70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    #Open and dilate the mask image
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
    
    #create mask to invert red color
    mask2 = cv2.bitwise_not(mask1)

    #segment the red part out of the frame using bitwise and with inverted mask
    res1 = cv2.bitwise_and(img, img, mask = mask2)

    # create image showning static background frame pixels only for the masked region
    res2 = cv2.bitwise_and(background, background,mask =mask1)

    # Generating the final output and writing
    finalOutput = cv2.addWeighted(res1, 1, res2, 1, 0)
    out.write(finalOutput)
    cv2.imshow("magic", finalOutput)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()
