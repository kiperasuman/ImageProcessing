import cv2
import numpy as np

# Görüntüyü yükleyin
image = cv2.imread('cat.jpg', 0)  # Gri tonlamalı olarak yükle

# Histogram eşitleme işlemi
equalized_image = cv2.equalizeHist(image)

# İlk görüntüyü ve eşitlenmiş görüntüyü yan yana gösterin
cv2.imshow('Original Image', image)
cv2.imshow('Gray Tone Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
