import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplace_blur(image, kernel_size):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Laplace filtresi uygula
    laplace_filtered = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=kernel_size)

    # Mutlak değer alarak negatif değerleri pozitife çevir
    laplace_filtered = np.abs(laplace_filtered)

    # Görüntüyü renkli hale getirme (BGR formatında)
    laplace_filtered_color = cv2.cvtColor(np.uint8(laplace_filtered), cv2.COLOR_GRAY2BGR)

    return laplace_filtered_color

image_path = "fruits.jpg"
image = cv2.imread(image_path)

# Laplace filtresi ile blurring işlemi uygula
blurred_image = laplace_blur(image, kernel_size=3)

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Color Image')

plt.subplot(122)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image with Laplace Filter')

plt.show()
