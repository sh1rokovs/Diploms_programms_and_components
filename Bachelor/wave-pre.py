from scipy.integrate import quad
from numpy import*
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
N=256
def S(t):
    return sin(2*pi*t/10)+sin(2*pi*t/50)
plt.title(' Сумма двух гармонических колебаний', size=12)
y=[S(t) for t in arange(0,250,1)]
x=[t for t in arange(0,250,1)]
plt.plot(x,y)
plt.grid()
plt.show()