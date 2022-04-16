from  numpy import*
import pandas as pd
from pylab import*
import scaleogram as scg
scg.set_default_wavelet('morl')
# Заменяя вейвлеты можно исследовать зависимость временного разрешения от масштаба
#scg.set_default_wavelet('cgau5')
#scg.set_default_wavelet('cgau1')
#scg.set_default_wavelet('shan0.5-2')
#scg.set_default_wavelet('mexh')
##Рассмотрим временную шкалу с 1 периодом / секунду
ns   = 1024
time = arange(ns)
scales = scg.periods2scales(arange(1, 40))
allwaves = np.zeros(ns, dtype=np.float32)
periods = [10, 20, 40]
for i in range(0,3):
    allwaves += cos(2*np.pi/periods[i]*time)

fig1, ax1 = subplots(1, 1, figsize=(6.5,2))
lines = ax1.plot(allwaves); ax1.set_title("Три колебания одновременно")
ax1.set_xlim(0, len(time)); ax1.set_xlabel("Время")
fig1.tight_layout()
coikw = {'alpha': 0.5, 'hatch': '/'}
ax2 = scg.cws(allwaves, scales=scales, figsize=(7,2), coikw=coikw)
tight_layout()
show()
