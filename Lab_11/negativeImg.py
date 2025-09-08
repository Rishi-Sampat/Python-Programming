import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r'E:\College\Python Programming\Lab_11\bmw-e60-m5')
img_array = np.array(img)
is_grayscale = len(img_array.shape) < 3
def create_negative(image):
    if is_grayscale:
        negative_image = 255 - image
    else:
        negative_image = 255 - image
    return negative_image
negative_img = create_negative(img_array)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(negative_img)
plt.title('Negative Image')
plt.axis('off')
plt.tight_layout()
plt.show()