from numpy import *
import matplotlib.pyplot as plt

x = arange(-5, 5, 0.01)
#(1 / a ** 0.5) * exp(-0.5 * ((t - b) / a) ** 2) * (((t - b) / a) ** 2 - 1)


def w(t):
    f = (1 - t ** 2) * e ** ((-t ** 2) / 2)
    return f


plt.title("Вейвлет «Мексиканская шляпа»:\n$\Psi^{*}(t)=(1-t^{2})*e^{-t^{2}/2}$")
y = [w(t) for t in x]
plt.plot(x, y)
plt.legend(loc='best')
plt.grid(True)
plt.show()
