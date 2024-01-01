import numpy as np
import cv2
import matplotlib.pyplot as plt

def separative_mean_filter(image, window_size):
    filtered_image = np.zeros_like(image, dtype=np.float64)

    pad_size = window_size // 2
    padded_image = np.pad(image, ((pad_size, pad_size), (pad_size, pad_size), (0, 0)), mode='constant', constant_values=0)

    for i in range(pad_size, padded_image.shape[0] - pad_size):
        for j in range(pad_size, padded_image.shape[1] - pad_size):
            for k in range(3):  # 3 renk kanalı (RGB)
                window = padded_image[i-pad_size:i+pad_size+1, j-pad_size:j+pad_size+1, k]
                filtered_image[i-pad_size, j-pad_size, k] = np.mean(window)

    return np.clip(filtered_image, 0, 255).astype(np.uint8)


image_path = "cat.jpeg"
original_image = cv2.imread(image_path)

window_size = 3
filtered_image = separative_mean_filter(original_image, window_size)

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.title('RGB Filtering')

plt.show()
