import csv
from numpy import*
import pandas as pd
from pylab import*
import scaleogram as scg
#scg.set_default_wavelet('cmor1-1.5')
# Заменяя вейвлеты можно исследовать зависимость временного разрешения от масштаба
scg.set_default_wavelet('morl')
#scg.set_default_wavelet('cgau1')
#scg.set_default_wavelet('shan0.5-2')
#scg.set_default_wavelet('mexh')


list_with_time = []
list_with_amp = []

with open('data1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_with_time.append(float(row['time']))
        list_with_amp.append(float(row['amp']))


ns = len(list_with_time)
time = arange(0.01, 2.19, 0.01)
print(time)

scales = scg.periods2scales(arange(10, 60, 1))
fig1, ax1 = subplots(1, 1, figsize=(6.5, 2))
lines = ax1.plot(list_with_amp)
ax1.set_title("ЭКГ")

ax1.set_xlim(0.01, 2.19, 0.01)
ax1.set_xlabel("Время")

fig1.tight_layout()
coikw = {'alpha': 0.5, 'hatch': '/'}
ax2 = scg.cws(list_with_amp, figsize=(7, 2), coikw=coikw)
tight_layout()
show()
