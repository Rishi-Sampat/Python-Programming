import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
img=Image.open(r'E:\College\Python Programming\Lab_11\bmw-e60-m5')
img_array = np.array(img)
threshold = 128
binary_img = np.where(img_array < threshold, 0, 255).astype(np.uint8)
plt.figure(figsize= (10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(binary_img, cmap='gray')
plt.title('Binarized Image (Threshold = 128)')
plt.axis('off')
plt.tight_layout()
plt.show()