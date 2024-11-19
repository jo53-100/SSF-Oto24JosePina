# Simulación de Sistemas Físicos, Tarea 3 Inciso 'a'

import numpy as np
import matplotlib.pyplot as plt

def plot_function(epsilon, tolerance=0.1, max_iterations=100):
    """Finds the smallest n such that the maximum difference between functions at n and n + 10 nodes is less than tolerance.

    Args:
        epsilon (float): Positive constant parameter for function behavior.
        tolerance (float, optional): Maximum allowed difference between functions. Defaults to 0.1.
        max_iterations (int, optional): Maximum iterations to prevent infinite loop. Defaults to 100.

    Returns:
        tuple: (final_n, final_difference), where final_n is the smallest n for the tolerance condition.
    """

    n = 10  # Initial value of n
    difference = tolerance  # Initialize difference to enter the loop

    while difference >= tolerance and n < max_iterations:
        # Define x values for n+1 and n+11 points
        x_n = np.linspace(epsilon, 1, n + 1)
        x_n_plus_10 = np.linspace(epsilon, 1, n + 11)

        # Compute function values
        f_x_n = np.sin(1 / (x_n + epsilon))
        f_x_n_plus_10 = np.sin(1 / (x_n_plus_10 + epsilon))

        # Interpolate to align the arrays and calculate the maximum difference
        f_x_n_plus_10_interp = np.interp(x_n, x_n_plus_10, f_x_n_plus_10)
        difference = np.max(np.abs(f_x_n - f_x_n_plus_10_interp))

        # Check if the condition is satisfied, if not increment n
        if difference >= tolerance:
            n += 1  # Increment n to get closer to tolerance

    # Final plot with the smallest n that meets the condition
    plt.plot(x_n, f_x_n, label=f'n = {n}')
    plt.plot(x_n, f_x_n_plus_10_interp, label=f'n + 10 = {n + 10}')
    plt.title(r'$f(x) = \sin\left(\frac{1}{x + \epsilon}\right)$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Return the final n and the last computed difference for verification
    return n, difference

# Example usage for question (c)
epsilon = 1/20  # Input parameter ε > 0
tolerance = 0.1  # Tolerance level for difference

n, final_difference = plot_function(epsilon, tolerance)
print(f"Final n: {n}, Maximum difference: {final_difference:.4f}")

