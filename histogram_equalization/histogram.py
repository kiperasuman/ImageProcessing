import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = 'image_low_contrast.jpg'
new_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme işlemi
equalized_image = cv2.equalizeHist(new_image)

# Orjinal ve eşitlenmiş görüntüleri gösteren subplot'lar oluştur
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(new_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()
