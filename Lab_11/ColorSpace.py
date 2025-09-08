import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
img=Image.open(r'E:\College\Python Programming\Lab_11\bmw-e60-m5')
img_array = np.array(img)
gray_img = np.dot (img_array[..., :3], [0.299, 0.587, 0.114])
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original RGB Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.tight_layout()
plt.show()