import cv2
import numpy as np

frame = cv2.imread('imgs/00Origin.bmp')

# laplacian = cv2.Laplacian(frame, cv2.CV_64F)
# sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
# sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
edges = cv2.Canny(frame, 100, 100)

final = cv2.bitwise_not(edges)
# cv2.imshow('original', frame)
# cv2.imshow('laplacian', laplacian)
# cv2.imshow('sobelx', sobelx)
# cv2.imshow('sobely', sobely)
cv2.imshow('edges',edges)
cv2.imshow('invert',final)
    
cv2.waitKey()
cv2.destroyAllWindows()

# cap.release()