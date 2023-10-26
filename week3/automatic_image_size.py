import cv2
import numpy
import matplotlib

cv2.namedWindow("Resize Image")
img = cv2.imread("opencv.png")
img = cv2.resize(img ,(150,245))
cv2.imshow("Resize Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
