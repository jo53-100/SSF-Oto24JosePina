from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt, floating
from scipy.stats import norm

# Example data
data = loadtxt(r'C:\Users\shipp\PycharmProjects\Simulacion_de_Sistemas\altura6.dat', float)
sorted_data = np.sort(data)

mean = np.mean(data)
median = np.median(data)
std_dev: floating[Any] = np.std(data)
# Create histogram

plt.hist(data, bins=50, density=True, alpha=0.6, color='b', edgecolor='black')

# Generate values for the Gaussian curve
xmin, xmax = plt.xlim()  # Get the x-axis range
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, mean, std_dev)

# Plot the Gaussian curve
plt.plot(x, y, 'r-', label=f'Gaussian fit: Mean={mean:.2f}, Std={std_dev:.2f}')

# Add title and labels
plt.title("Height Data with Gaussian Fit")
plt.xlabel("Height")
plt.ylabel("Density")

# Add legend
plt.legend()

# Show plot
plt.show()
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
