import csv

import pywt
import numpy as np
import matplotlib.pyplot as plt

#t = np.linspace(0, 1, 200)

list_with_amp = []
list_with_time = []

with open('data1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_with_time.append(float(row['time']))
        list_with_amp.append(float(row['amp']))

signal = list_with_amp
t = list_with_time

scales = np.arange(1, 10)
coef, freqs = pywt.cwt(signal, scales, 'morl')

plt.figure(figsize=(15, 10))
plt.imshow(abs(coef), interpolation='bilinear', cmap='binary', aspect='auto',
           vmax=abs(coef).max(), vmin=-abs(coef).max())
plt.xlabel(f'(wave-ecg.py)')
plt.show()

plt.figure(figsize=(15, 10))
plt.plot(t, signal)
plt.grid(color='gray', linestyle=':', linewidth=0.5)
plt.show()
