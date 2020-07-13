import numpy as np
import cv2

cap = cv2.VideoCapture('imgs/people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    
    fgmask = fgbg.apply(frame)
    # rgb_img = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
    background = fgbg.getBackgroundImage()
    background = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY)
    # fgmask = fgmask.reshap((540,960,3))

    both = np.concatenate((fgmask, background), axis=1)
    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', fgmask)
    cv2.imshow('shadows', both)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()