import numpy as np
import matplotlib.pyplot as plt


def plot_function(epsilon, n, tolerance=0.1):
    # Create a while loop to find the smallest n where the difference is less than the tolerance
    difference = tolerance
    while difference >= tolerance:
        # Define the unit interval and create n + 1 and n + 11 equally spaced nodes
        x_n = np.linspace(epsilon, 1, n + 1)
        x_n_plus_10 = np.linspace(epsilon, 1, n + 11)

        # Compute the function values for both n and n + 10
        f_x_n = np.sin(1 / (x_n + epsilon))
        f_x_n_plus_10 = np.sin(1 / (x_n_plus_10 + epsilon))

        # Calculate the difference between the two functions at each point
        difference = np.max(np.abs(f_x_n - np.interp(x_n, x_n_plus_10, f_x_n_plus_10)))

        # Plot the two functions
        plt.plot(x_n, f_x_n, label=f'n = {n}')
        plt.plot(x_n_plus_10, f_x_n_plus_10, label=f'n + 10 = {n + 10}')

        # Increase n for the next iteration if necessary
        if difference >= tolerance:
            n += 1

    # Plot the functions when the difference condition is satisfied
    plt.title(r'$f(x) = \sin\left(\frac{1}{x + \epsilon}\right)$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

    return n, difference


# Example usage
epsilon = 0.1  # Input parameter ε > 0
initial_n = 100  # Starting value of n
tolerance = 0.1  # Tolerance level for the difference

n, final_difference = plot_function(epsilon, initial_n, tolerance)
print(f"Final n: {n}, Maximum difference: {final_difference:.4f}")

