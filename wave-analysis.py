import csv

import matplotlib.pyplot as plt
from numpy import *
import pywt
from scipy.fftpack import fft

list_with_time = []
list_with_amp = []

with open('data1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_with_time.append(float(row['time']))
        list_with_amp.append(float(row['amp']))


y = list_with_amp
x = list_with_time

sampling_rate = 1024
t = arange(0, 1.0, 1.0 / sampling_rate)
f1 = 100
f2 = 150
wavename = 'morl'
totalscal = 256

data = piecewise(t, [t < 1, t < 0.5], [lambda t: sin(2 * pi * f1 * t), lambda t: sin(2 * pi * f2 * t)])

yf = abs(fft(data))
xf = arange(len(data))

fc = pywt.central_frequency(wavename)
cparam = 2 * fc * totalscal
scales = arange(1, 14, 1)

[cwtmatr, frequencies] = pywt.cwt(y, scales, wavename)

plt.figure(figsize=(8, 4))
plt.subplot(211)
plt.plot(t, data)
plt.xlabel(f'Время(с)')
plt.title(f'Сигнал 100Hz и 150Hz')

plt.subplot(212)
plt.contourf(x, frequencies, abs(cwtmatr))
plt.ylabel(f'Частота(Hz)')
plt.xlabel(f'Время(с)\n(wave-analysis.py)')
plt.subplots_adjust(hspace=0.4)

plt.figure()
plt.plot(xf, yf, color="red")
plt.title('Преобразование Фурье')
plt.xlabel(f'(wave-analysis.py)')
plt.show()
