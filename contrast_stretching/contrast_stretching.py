import cv2
import numpy as np
import matplotlib.pyplot as plt


def contrast_stretching(image):
    # Görüntünün minimum ve maksimum piksel değerlerini bulma
    min_val = np.min(image)
    max_val = np.max(image)

    # Kontrast genişletme formülü
    stretched_image = 255 * ((image - min_val) / (max_val - min_val))

    # Noktadan noktaya kayan virgül işlemleri için piksel değerlerini tamsayıya dönüştürme
    stretched_image = stretched_image.astype(np.uint8)

    return stretched_image


# Görüntüyü okuma
image_path = "cat.jpeg"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Kontrast genişletme uygulama
contrast_stretched_image = contrast_stretching(original_image)

# Görüntüleri matplotlib kullanarak gösterme
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(contrast_stretched_image, cmap='gray')
plt.title('Contrast Stretched Image')

plt.show()
