import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1400)

y = 7 * np.sin(2 * np.pi * 180 * x) + 1.5 * np.sin(2 * np.pi * 390 * x) + 5.1 * np.sin(2 * np.pi * 600 * x)

yf = abs(fft(y))  # Модуль
xf = np.arange(len(y))  # Частота

plt.figure()
plt.plot(xf, yf, color="red")
plt.title(f'Преобразование Фурье')
plt.xlabel(f'(furie-pre.py)')

plt.figure()
plt.plot(x[0:50], y[0:50], color="red")
plt.title(f'Исходный сигнал')
plt.xlabel(f'(furie-pre.py)')

plt.show()
