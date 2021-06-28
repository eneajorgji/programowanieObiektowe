import numpy as np
from scipy.integrate import simps, trapz
import matplotlib.pyplot as plt


def f(x):
    return x ** 2


fig, ax = plt.subplots(1, 1)

# Continous curve
x = np.arange(0, 9, 0.01)
y = f(x)
ax.plot(y, x, 'k-')

# Trapizium
xstep = np.arange(0, 10, 3)
area = trapz(y, x)
print(area)
ax.fill_between(f(xstep), 0, xstep)

# Simpsons
area = simps(y, x)
print(area)
# etc etc

plt.show()
