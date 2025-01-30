import numpy as np
from scipy.integrate import quad

def integrand(x):
    return 1 / ((1 + x) * np.sqrt(x))

result, _ = quad(integrand, 0, np.inf)

print(f"Pi is {result:.8f}")
difference = np.pi - result
print(f"Difference from numpy.pi is: {difference:.15f}")