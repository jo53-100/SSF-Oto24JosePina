import numpy as np
import scipy.integrate as integrate

# Define the function
def integrand(x):
    return np.exp(4 * x)

# Exact value of the integral (for verification)
I_exact = (np.exp(4) - 1) / 4  # Exact value of the integral

# Integration using SciPy's quad function
def compute_integral(epsilon):
    result, error = integrate.quad(integrand, 0, 1)  # Computes the integral
    return result, error

# Run the computation for different values of epsilon
epsilons = [1/100, 1/1000, 1/10000]
for epsilon in epsilons:
    result, error = compute_integral(epsilon)
    print(f"Estimated Integral: {result:.6f}, Error estimate: {error:.6f}")
    print(f"Exact Integral: {I_exact:.6f}, Difference: {abs(I_exact - result):.6f}")
