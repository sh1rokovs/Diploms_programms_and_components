import matplotlib.pyplot as plt
import pywt

wavelet = pywt.ContinuousWavelet('mexh')
psi, x = wavelet.wavefun()
plt.plot(x, psi)
plt.title(f'Вейвлет \"Мексиканская шляпа\"')
plt.xlabel(f'(mexh-wave.py)')
plt.show()