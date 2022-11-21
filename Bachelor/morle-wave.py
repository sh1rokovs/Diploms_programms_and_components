import matplotlib.pyplot as plt
import pywt

wavelet = pywt.ContinuousWavelet('morl')
psi, x = wavelet.wavefun()
plt.plot(x, psi)
plt.title(f'Вейвлет Морле')
plt.xlabel(f'(morle-wave.py)')
plt.show()
