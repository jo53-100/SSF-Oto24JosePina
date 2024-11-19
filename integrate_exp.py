import numpy as np
import matplotlib.pyplot as plt

# Define the function to integrate
def f(x):
    return np.exp(-x**2)

# Gauss-Legendre quadrature for finite limits
def gauss_legendre_finite(f, a, b, n):
    # Get Gauss-Legendre nodes and weights for [-1, 1]
    t, w = np.polynomial.legendre.leggauss(n)

    # Transform nodes and weights to [a, b]
    x = 0.5 * (t + 1) * (b - a) + a  # Map t to x in [a, b]
    weights = 0.5 * (b - a) * w

    # Compute the integral
    integral = sum(weights * f(x))
    return integral
# X values from -10 to 10
x_vals = np.linspace(-10, 10, 500)
y_vals = f(x_vals)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$e^{-x^2}$", color="blue")
plt.title("Plot of $e^{-x^2}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend()
plt.grid(True)
plt.show()

# Exact value of the integral
exact_value = np.sqrt(np.pi)

# Parameters
n_values = [100, 200, 300, 400, 500]  # Number of Gauss-Legendre points
L_values = [1, 2, 4, 6, 8, 10]  # Upper limits of integration

# Store results
results = {}

for n in n_values:
    results[n] = []
    for L in L_values:
        integral = 2 * gauss_legendre_finite(f, 0, L, n)  # Exploit symmetry
        error = abs(exact_value - integral)
        results[n].append((L, integral, error))

# Create the table
print("Table of T(n, L) and errors:")
print(f"{'n':>2} {'L':>4} {'T(n, L)':>12} {'Error':>12}")
for n in n_values:
    for L, integral, error in results[n]:
        print(f"{n:>2} {L:>4} {integral:>12.8f} {error:>12.8f}")

