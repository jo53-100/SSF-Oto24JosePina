import numpy as np
import matplotlib.pyplot as plt

# Function f(x) and its exact derivative
def f(x, epsilon):
    return np.sin(1 / (x + epsilon))

def f_exact_derivative(x, epsilon):
    return -np.cos(1 / (x + epsilon)) / (x + epsilon)**2

# Finite difference approximation
def finite_difference(f, x, epsilon, h):
    return (f(x + h, epsilon) - f(x, epsilon)) / h

# Parameters
epsilon = 1 / 5  # Change as needed
n = 10           # Initial number of points
h = 1e-5         # Small step size for finite difference
tolerance = 0.1  # Tolerance for difference

# (a) Create x values and compute derivatives
def compute_and_plot(n, epsilon):
    x = np.linspace(0, 1, n, endpoint=False)[1:]  # Avoid x=0 (division by zero)
    x_mid = (x[:-1] + x[1:]) / 2                  # Midpoints for finite difference
    exact = f_exact_derivative(x_mid, epsilon)
    approx = finite_difference(f, x_mid, epsilon, h)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(x_mid, exact, label="Exact Derivative", linestyle='-', color='blue')
    plt.plot(x_mid, approx, label="Finite Difference Approximation", linestyle='--', color='red')
    plt.title(f"Derivative Approximation (n={n}, ε={epsilon})")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.legend()
    plt.grid()
    plt.show()

    return exact, approx

# (b) Test with n=10 and epsilon=1/5
print("Testing with n=10 and ε=1/5:")
exact, approx = compute_and_plot(n, epsilon)

# (c) Find n for tolerance
def find_n_for_tolerance(epsilon, tolerance):
    n = 10
    while True:
        x = np.linspace(0, 1, n, endpoint=False)[1:]  # Avoid x=0 (division by zero)
        x_mid = (x[:-1] + x[1:]) / 2                  # Midpoints for finite difference
        exact = f_exact_derivative(x_mid, epsilon)
        approx = finite_difference(f, x_mid, epsilon, h)

        # Check the maximum difference
        max_diff = np.max(np.abs(exact - approx))
        if max_diff < tolerance:
            break
        n += 1

    print(f"Minimum n for ε={epsilon} and tolerance={tolerance}: n = {n}")
    compute_and_plot(n, epsilon)
    return n

# Finding n for ε=1/5, ε=1/10, and ε=1/20
epsilons = [1/5, 1/10, 1/20]
for eps in epsilons:
    print(f"\nFinding n for ε={eps}:")
    find_n_for_tolerance(eps, tolerance)

# (f) Experimentally analyze large n and small ε
epsilon = 1 / 50
n_large = 200
print(f"\nTesting with large n={n_large} and ε={epsilon}:")
compute_and_plot(n_large, epsilon)
