import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image

image = Image.open('img4.jpg')
image = np.array(image.getdata())

# make the data
x = image[0:2000:2]
y = image[1:2000:2]

# plot
fig, ax = plt.subplots()

plt.ylabel(f'Нечетные пиксели')
plt.xlabel(f'Четные пиксели\n(pixels.py)')
ax.scatter(x, y, s=3)

plt.show()
