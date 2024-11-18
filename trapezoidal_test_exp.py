## El doc pide que sea por Gauss-Legendre
## Este programita hace por varios tipos

import numpy as np

# Define the function to integrate
def f(x):
    return np.exp(4 * x)

# Gauss-Legendre quadrature function
def gauss_legendre(f, a, b, n):
    # Get the Gauss-Legendre nodes and weights
    [x, w] = np.polynomial.legendre.leggauss(n)

    # Map the nodes and weights from [-1, 1] to [a, b]
    x_mapped = 0.5 * (x + 1) * (b - a) + a
    w_mapped = 0.5 * (b - a) * w

    # Compute the integral as the weighted sum
    integral = sum(w_mapped[i] * f(x_mapped[i]) for i in range(n))
    return integral

# Exact value of the integral
a_exact = (np.exp(4) - 1) / 4

# Integration limits
a = 0  # Lower limit
b = 1  # Upper limit

# Tolerances and corresponding calculations
epsilons = [1 / 100, 1 / 1000, 1 / 10000]

print("Using Gauss-Legendre Quadrature:")
for epsilon in epsilons:
    n = 2  # Start with n = 2 points
    while True:
        # Compute the integral using n Gauss-Legendre nodes
        a_n = gauss_legendre(f, a, b, n)
        error = abs(a_exact - a_n)

        # Check if the error meets the tolerance
        if error <= epsilon:
            break
        n += 1

    print(f"For ε = {epsilon}, n = {n} points yields |a - a(n)| <= ε")

