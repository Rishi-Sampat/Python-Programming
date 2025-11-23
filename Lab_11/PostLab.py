import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("E:/College/Python Programming/Lab_11/bmw-e60-m5.jpg")
img_array = np.array(img)

print("Dimensions (H x W x C):", img_array.shape)
print("Shape of image:", img_array.shape)

min_blue = img_array[:,:,2].min()
print("Minimum pixel value in Blue channel:", min_blue)


img = Image.open("E:/College/Python Programming/Lab_11/bmw-e60-m5.jpg").convert("RGB")
img_array = np.array(img)

padded_array = np.pad(
    img_array,
    pad_width=((100,100),(100,100),(0,0)),  # (rows, cols, channels)
    mode='constant',
    constant_values=0  # black
)

padded_img = Image.fromarray(padded_array)

plt.imshow(padded_img)
plt.title("With Black Padding (np.pad)")
plt.axis("off")
plt.show()



img = Image.open("E:/College/Python Programming/Lab_11/bmw-e60-m5.jpg")
img_array = np.array(img)

R = img_array[:,:,0]
G = img_array[:,:,1]
B = img_array[:,:,2]

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Red Channel")
plt.imshow(R, cmap="Reds")
plt.axis("off")

plt.subplot(1,3,2)
plt.title("Green Channel")
plt.imshow(G, cmap="Greens")
plt.axis("off")

plt.subplot(1,3,3)
plt.title("Blue Channel")
plt.imshow(B, cmap="Blues")
plt.axis("off")

plt.show()
