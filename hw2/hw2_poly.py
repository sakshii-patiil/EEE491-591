import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad 

def polynomial(x, a, b, c):
    return a * x**2 + b * x + c

def integral_polynomial(r, a, b, c):
    result = np.zeros_like(r)
    for i, ri in enumerate(r):
        result[i], _ = quad(polynomial, 0, ri, args=(a, b, c))  # Use quad here
    return result

r_values = np.arange(0, 5.01, 0.01)

a1, b1, c1 = 2, 3, 4
integral_values1 = integral_polynomial(r_values, a1, b1, c1)

a2, b2, c2 = 2, 1, 1
integral_values2 = integral_polynomial(r_values, a2, b2, c2)

plt.plot(r_values, integral_values1, label=f'a={a1}, b={b1}, c={c1}')
plt.plot(r_values, integral_values2, label=f'a={a2}, b={b2}, c={c2}')

plt.xlabel('r')
plt.ylabel('ax^2 + bx + c')
plt.title('hw2 poly')
plt.legend()

plt.show()