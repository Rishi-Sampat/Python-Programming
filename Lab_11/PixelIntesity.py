import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
img=Image.open(r'E:\College\Python Programming\Lab_11\bmw-e60-m5')
img_array = np.array(img)
hist, bins = np.histogram(img_array.flatten(), bins=256, range= (0, 256))
plt.figure(figsize=(10, 5))
plt.hist(img_array.flatten(), bins=256, range= (0, 256), density=True, color='gray')
plt.xlabel('Pixel Intensity')
plt.ylabel('Normalized Frequency')
plt.title('Histogram of Grayscale Image')
plt.grid(True)
plt.show()