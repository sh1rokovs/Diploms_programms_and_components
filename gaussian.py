from matplotlib import pyplot as plt
import numpy as np


def gaussian(x, mu, sig):
    return np.exp(-np.power((x - mu)/sig, 2.)/2.)


plt.title(f'Гауссиан')
plt.xlabel(f'(gaussian.py)')
for mu, sig in [(-1, 1)]:
    plt.plot(gaussian(np.linspace(-5, 3, 120), mu, sig))

plt.show()
