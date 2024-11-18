import numpy as np
import math


def f(x):
    return (math.e ** ((-x ** 2) / 2)) / ((2 * math.pi) ** 0.5)

# Exact value of the integral (Gaussian integral from -1 to 1)
I_exact = 0.682689492137086  # Known value of the integral

def trapezoidal_rule(f, a, b, n):
    # Tamaño del paso
    h = (b - a) / n

    # Evaluamos limites
    resultado = 0.5 * (f(a) + f(b))

    # Evaluamos los puntos dentro del intervalo
    for i in range(1, n):
        resultado += f(a + i * h)

    # Multiplicamos por el paso
    resultado *= h

    return resultado


# Simpson's Rule function
def simpsons_rule(f, a, b, n):
    # Ensure n is even
    if n % 2 != 0:
        raise ValueError("n must be an even number.")

    # tamaño del paso
    h = (b - a) / n

    # Evaluamos los limites
    resultado = f(a) + f(b)

    # Evaluate the odd points (multiplied by 4)
    for i in range(1, n, 2):
        resultado += 4 * f(a + i * h)

    # Evaluate the even points (multiplied by 2)
    for i in range(2, n, 2):
        resultado += 2 * f(a + i * h)

    # Multiply by h/3
    resultado *= h / 3

    return resultado


# Gauss-Legendre quadrature function
def gauss_legendre(f, a, b, n):
    # Get the Gauss-Legendre nodes and weights
    [x, w] = np.polynomial.legendre.leggauss(n)

    # Change of variables from [-1, 1] to [a, b]
    x_mapped = 0.5 * (x + 1) * (b - a) + a
    w_mapped = 0.5 * (b - a) * w

    # Compute the weighted sum of f(x) values
    integral = sum(w_mapped[i] * f(x_mapped[i]) for i in range(n))

    return integral


# Uso
a = -1  # Lower limit
b = 1  # Upper limit
n_valores = [6, 16]  # Number of trapezoids

print('Comparación de métodos numéricos de integración:')
for n in n_valores:
    # Trapezoidal rule
    I_trap = trapezoidal_rule(f, a, b, n)
    error_trap = abs(I_exact - I_trap)

    # Simpson's rule (ensure n is even)
    I_simp = simpsons_rule(f, a, b, n)
    error_simp = abs(I_exact - I_simp)

    # Gauss-Legendre quadrature
    I_gauss = gauss_legendre(f, a, b, n)
    error_gauss = abs(I_exact - I_gauss)

    print(f"Valor aproximado con {n} subintervalos usando la regla del trapezoide: {I_trap:.6f}, Error: {error_trap:.6f}")
    print(f"Valor aproximado con {n} subintervalos usando la regla de Simpson: {I_simp:.6f}, Error: {error_simp:.6f}")
    print(f"Valor aproximado con {n} subintervalos usando Gauss_Legendre: {I_gauss:.6f}, Error: {error_gauss:.6f}")

