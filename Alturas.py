import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt

# Example data
data = loadtxt(r'C:\Users\shipp\PycharmProjects\Simulacion_de_Sistemas\altura6.dat', float)
sorted_data = np.sort(data)

mean= np.mean(data)
median =np.median(data)
std_dev= np.std(data)
# Create histogram

plt.hist(sorted_data, bins=50, edgecolor='black')


# Add title and labels
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show plot
plt.show()
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")