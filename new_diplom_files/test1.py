import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import pywt

# image = Image.open('4(1).jpg')
# image = Image.open('img4.jpg')
image = Image.open('img2.jpg')
image_list = np.array(image.getdata()) # Диапазон яркостей — [0, 1]
print(image.size)
image1 = []

for el in range(image.size[0]):
    image1.append([image_list[el * image.size[0]:el * image.size[0] + image.size[0] - 1]])

print(image1)
