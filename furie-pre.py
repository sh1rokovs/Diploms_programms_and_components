import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt


# Выберите 1400 точек выборки,
# потому что установленная частотная
# составляющая сигнала составляет до 600 Гц.
# Согласно теореме выборки,
# частота выборки более чем в два раза
# превышает частоту сигнала,
# поэтому частота выборки
# установлена на 1400 Гц
# (то есть 1400 точек выборки за одну секунду)

x = np.linspace(0, 1, 1400)

# Установите сигнал для дискретизации,
# частотные составляющие 180, 390 и 600

y = 7 * np.sin(2 * np.pi * 180 * x) + 1.5 * np.sin(2 * np.pi * 390 * x) + 5.1 * np.sin(2 * np.pi * 600 * x)

yf = abs(fft(y))  # Modul
xf = np.arange(len(y))  # Частота

plt.figure()
plt.plot(xf, yf, color="red")
plt.title(f'Преобразование Фурье')
plt.xlabel(f'(furie-pre.py)')

plt.figure()
plt.plot(x[0:50], y[0:50])
plt.title(f'Исходный сигнал')
plt.xlabel(f'(furie-pre.py)')

plt.show()
