import math
import numpy as np
from scipy.integrate import quad

# Function for e^x / x
def f1(x):
    return np.exp(x) / x if x != 0 else 0  # Avoid division by zero

# Function for (1 - e^x) / x
def f2(x):
    return (1 - np.exp(x)) / x if x != 0 else 1  # Handling x = 0 to avoid division by zero

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    resultado = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        resultado += f(a + i * h)
    resultado *= h
    return resultado

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be an even number.")
    h = (b - a) / n
    resultado = f(a) + f(b)
    for i in range(1, n, 2):
        resultado += 4 * f(a + i * h)
    for i in range(2, n, 2):
        resultado += 2 * f(a + i * h)
    resultado *= h / 3
    return resultado

def gauss_legendre(f, a, b, n):
    [x, w] = np.polynomial.legendre.leggauss(n)
    x_mapped = 0.5 * (x + 1) * (b - a) + a
    w_mapped = 0.5 * (b - a) * w
    integral = sum(w_mapped[i] * f(x_mapped[i]) for i in range(n))
    return integral

# Compute reference values using SciPy's quad for high precision
ref_val1, _ = quad(lambda x: np.exp(x) / x, 1e-10, 5)
ref_val2, _ = quad(lambda x: (1 - np.exp(x)) / x, 1e-10, 5)

# Limits of integration
a = 1e-10  # Lower limit to avoid division by zero
b = 5

# Number of intervals for numerical integration
n_valores = [6, 16]  # Number of intervals

# Compare methods for the integral of e^x / x
print('Comparación de métodos numéricos de integración para e^x / x:')
for n in n_valores:
    # Trapezoidal rule
    I_trap1 = trapezoidal_rule(f1, a, b, n)
    error_trap1 = abs(ref_val1 - I_trap1)
    print(f"Valor aproximado con {n} subintervalos usando la regla del trapezoide para e^x / x: {I_trap1:.6f}, Error: {error_trap1:.6f}")

    # Simpson's rule (ensure n is even)
    I_simp1 = simpsons_rule(f1, a, b, n)
    error_simp1 = abs(ref_val1 - I_simp1)
    print(f"Valor aproximado con {n} subintervalos usando la regla de Simpson para e^x / x: {I_simp1:.6f}, Error: {error_simp1:.6f}")

    # Gauss-Legendre quadrature
    I_gauss1 = gauss_legendre(f1, a, b, n)
    error_gauss1 = abs(ref_val1 - I_gauss1)
    print(f"Valor aproximado con {n} subintervalos usando Gauss-Legendre para e^x / x: {I_gauss1:.6f}, Error: {error_gauss1:.6f}")

# Compare methods for the integral of (1 - e^x) / x
print('\nComparación de métodos numéricos de integración para (1 - e^x) / x:')
for n in n_valores:
    # Trapezoidal rule
    I_trap2 = trapezoidal_rule(f2, a, b, n)
    error_trap2 = abs(ref_val2 - I_trap2)
    print(f"Valor aproximado con {n} subintervalos usando la regla del trapezoide para (1 - e^x) / x: {I_trap2:.6f}, Error: {error_trap2:.6f}")

    # Simpson's rule (ensure n is even)
    I_simp2 = simpsons_rule(f2, a, b, n)
    error_simp2 = abs(ref_val2 - I_simp2)
    print(f"Valor aproximado con {n} subintervalos usando la regla de Simpson para (1 - e^x) / x: {I_simp2:.6f}, Error: {error_simp2:.6f}")

    # Gauss-Legendre quadrature
    I_gauss2 = gauss_legendre(f2, a, b, n)
    error_gauss2 = abs(ref_val2 - I_gauss2)
    print(f"Valor aproximado con {n} subintervalos usando Gauss-Legendre para (1 - e^x) / x: {I_gauss2:.6f}, Error: {error_gauss2:.6f}")
