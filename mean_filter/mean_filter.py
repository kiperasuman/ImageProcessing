import cv2
import numpy as np
import matplotlib.pyplot as plt

def ortalama_filtre(image, kernel_size):
   return cv2.blur(image, (kernel_size, kernel_size))

image = "fruits.jpg"
image_read = cv2.imread(image)

filtered_image = ortalama_filtre(image_read, kernel_size=3)

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(122)
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.title('Filtered Image')

plt.show()
