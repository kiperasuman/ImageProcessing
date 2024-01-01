import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('cat.jpg')

# Kenar algılama filtresi (örneğin Sobel filtresi)
kernel = np.array([[-1, -2, -1],
                  [0, 0, 0],
                  [1, 2, 1]])

# Görüntüyü gri tonlamalı hale getir
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Konvolüsyon işlemini uygula
edges = cv2.filter2D(gray_image, -1, kernel)

# Sonucu göster
cv2.imshow('Kenarlar', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
