import numpy as np
from scipy.integrate import quad

def func(z):
    return 1 / (np.sqrt((1 - z) * z))

integral, error = quad(func, 0, 1)

print("Pi is {:,.8f}".format(integral))
print("Difference from numpy.pi is: {:,.15f}".format(np.pi - integral))