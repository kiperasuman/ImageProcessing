import cv2
import numpy as np


img = cv2.imread("cat.jpg")
cv2.imshow("Original Image", img)

height,width = img.shape[:2]

start_row,start_column = int(height*0.3),int(width*0.30)
end_row,end_column = int(height*0.6),int(width*0.77)

new_image = img[start_row:end_row , start_column:end_column]
cv2.imshow("Cropped Image",new_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
