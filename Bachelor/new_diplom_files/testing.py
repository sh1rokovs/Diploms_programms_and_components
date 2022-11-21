import os

import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data
import matplotlib.cbook as cbook

import os
from PIL import Image

im = Image.open("img.png")

# Load image
# original = pywt.data.camera()
# original = im.getdata()

# ///////////////////
with cbook.get_sample_data('C:/Users/Sid/PycharmProjects/diplom/new_diplom_files/img2.jpg') as image_file:
    original = plt.imread(image_file)
# //////////////////

# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(original, 'bior1.3')
LL, (LH, HL, HH) = coeffs2
fig = plt.figure(figsize=(12, 3))
for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(1, 4, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

fig.tight_layout()
plt.show()
