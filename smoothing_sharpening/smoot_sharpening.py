import cv2
import numpy as np
import matplotlib.pyplot as plt


def smoothing_f(image, kernel_size):
      return cv2.blur(image, (kernel_size, kernel_size))
def sharpening_f(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    sharpened_image = image - 0.5 * laplacian
    sharpened_image = sharpened_image.astype(np.uint8)
    return sharpened_image

image_path = "fruits.jpg"
original_image = cv2.imread(image_path)

# Yumuşatma işlemi
smoothed_image = smoothing_f(original_image, kernel_size=3)

# Keskinleştirme işlemi
sharpened_image = sharpening_f(original_image)

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(132)
plt.imshow(cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB))
plt.title('Smoothed Image')

plt.subplot(133)
plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
plt.title('Sharpened Image')

plt.show()
