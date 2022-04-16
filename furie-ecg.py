import csv
from numpy import *
from scipy.fftpack import fft
import matplotlib.pyplot as plt

list_with_time = []
list_with_amp = []

with open('data1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_with_time.append(float(row['time']))
        list_with_amp.append(float(row['amp']))


print(list_with_time)
print(list_with_amp)

x = arange(list_with_time[0], list_with_time[-1], 0.01)


def w(t):
    return list_with_amp[t]


y = [w(t) for t in range(len(list_with_amp) - 1)]

yf = abs(fft(y))  # Modul
xf = arange(len(y))  # Частота

plt.figure()
plt.plot(xf, yf, color="red")
plt.title('Преобразование Фурье')

plt.figure()
plt.plot(x, y)
plt.title('Исходный сигнал')

plt.show()
