from math import sqrt

from matplotlib import pyplot as plt
import numpy as np
import PIL.Image as Image
from matplotlib.pyplot import imshow

image = Image.open('img4.jpg').convert('L')
image = np.array(image.getdata()) / 255.0


def create_matrix(massive):
    image = []
    for el in range(int(np.sqrt(len(massive)))):
        image.append([])
        for elem in range(int(np.sqrt(len(massive)))):
            image[el].append(massive[el * int(np.sqrt(len(massive))) + elem])
    return np.array(image)


CL = [(1 + sqrt(3)) / (4 * sqrt(2)),
      (3 + sqrt(3)) / (4 * sqrt(2)),
      (3 - sqrt(3)) / (4 * sqrt(2)),
      (1 - sqrt(3)) / (4 * sqrt(2))]


def hpf_coeffs(CL):
    N = len(CL)
    CH = [(-1)**k * CL[N - k - 1] for k in range(N)]
    return CH


def pconv(data, CL, CH, delta=0):
    assert(len(CL) == len(CH))
    N = len(CL)
    M = len(data)
    out = []
    for k in range(0, M, 2):
        sL = 0
        sH = 0
        for i in range(N):
            sL += data[(k + i - delta) % M] * CL[i]
            sH += data[(k + i - delta) % M] * CH[i]
        out.append(sL)
        out.append(sH)
    return out


def icoeffs(CL, CH):
    assert(len(CL) == len(CH))
    iCL = []
    iCH = []
    for k in range(0, len(CL), 2):
        iCL.extend([CL[k-2], CH[k-2]])
        iCH.extend([CL[k-1], CH[k-1]])
    return iCL, iCH


def dwt2(image, CL):
    CH = hpf_coeffs(CL)
    w = len(image[0])
    h = len(image)
    imageT = image.copy()
    for i in range(h):
        imageT[i, :] = pconv(imageT[i, :], CL, CH)
    for i in range(w):
        imageT[:, i] = pconv(imageT[:, i], CL, CH)

    data = imageT.copy()
    data[0:int(h/2), 0:int(w/2)] = imageT[0:h:2, 0:w:2]
    data[int(h/2):h, 0:int(w/2)] = imageT[1:h:2, 0:w:2]
    data[0:int(h/2), int(w/2):w] = imageT[0:h:2, 1:w:2]
    data[int(h/2):h, int(w/2):w] = imageT[1:h:2, 1:w:2]
    return data


def idwt2(data, CL):
    w, h = data.shape

    imageT = data.copy()
    imageT[0:h:2, 0:w:2] = data[0:int(h/2), 0:int(w/2)]
    imageT[1:h:2, 0:w:2] = data[int(h/2):h, 0:int(w/2)]
    imageT[0:h:2, 1:w:2] = data[0:int(h/2), int(w/2):w]
    imageT[1:h:2, 1:w:2] = data[int(h/2):h, int(w/2):w]

    CH = hpf_coeffs(CL)
    iCL, iCH = icoeffs(CL, CH)
    image = imageT.copy()
    for i in range(w):
        image[:, i] = pconv(image[:, i], iCL, iCH, delta=len(iCL) - 2)
    for i in range(h):
        image[i, :] = pconv(image[i, :], iCL, iCH, delta=len(iCL) - 2)

    return image


data2 = dwt2(create_matrix(image), CL)
imshow(data2, cmap='gray')
plt.show()
plt.imsave("new_img4.jpg", data2, cmap='gray')

imshow(create_matrix(image), cmap='gray')
plt.show()
