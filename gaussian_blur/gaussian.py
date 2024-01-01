import cv2
import matplotlib.pyplot as plt

def apply_gaussian_blur(image, sigma=1.0):
    blurred_image = cv2.GaussianBlur(image, (5, 5), sigma)
    return blurred_image

# Görüntüyü oku
image_path = "cat.jpeg"
image = cv2.imread(image_path)

# Gaussian filtre uygula
blurred_image = apply_gaussian_blur(image, sigma=1.0)

# Görüntüleri gösterme
plt.figure(figsize=(8, 4))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(122)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image')

plt.show()
