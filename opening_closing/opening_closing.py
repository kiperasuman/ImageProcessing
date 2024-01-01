import cv2
import numpy as np
import matplotlib.pyplot as plt

def opening_closing_demo(image_path, operation_type, kernel_size):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Binarize et (thresholding)
    _, binary_image = cv2.threshold(original_image, 128, 255, cv2.THRESH_BINARY)

    # Morfolojik işlemler için kernel oluştur
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Açma  veya Kapatma  işlemleri
    if operation_type == 'Opening':
        result_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
    elif operation_type == 'Closing':
        result_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    else:
        raise ValueError("Geçersiz işlem.")

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Orijinal Görüntü')

    plt.subplot(1, 3, 2)
    plt.imshow(binary_image, cmap='gray')
    plt.title('Binarize Edilmiş Görüntü')

    plt.subplot(1, 3, 3)
    plt.imshow(result_image, cmap='gray')
    plt.title(f'{operation_type} İşlemi')

    plt.show()

image_path = "cat.jpeg"
opening_closing_demo(image_path, operation_type='Closing', kernel_size=3)
