import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image

image = Image.open('img4.jpg')
image = np.array(image.getdata())

x = (image[0:2000:2] + image[1:2000:2]) / 2
y = (image[1:2000:2] - image[0:2000:2]) / 2


# plot
fig, ax = plt.subplots()

plt.ylabel(f'Полуразности')
plt.xlabel(f'Полусуммы\n(sum-and-diff.py)')
ax.scatter(x, y, s=3)

plt.show()
