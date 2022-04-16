import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

fig, ax = plt.subplots()

plt.title(f'Синусоида')
plt.xlabel(f'(sinysoida.py)')
ax.plot(x, y)

plt.show()
