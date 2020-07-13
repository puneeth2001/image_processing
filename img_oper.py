import numpy as np
import cv2

img = cv2.imread('/home/puneeth/Desktop/main-qimg-419137b9e0589a397b3692769cb0e906.jpeg',cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]
print(px)

img[100:150,100:150] = [255,255,255]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()