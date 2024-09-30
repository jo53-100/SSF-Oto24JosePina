## Este programa saca estadísticas a partir de unas mediciones obtenidas
## En el laboratorio de electrónica, debajo del Dr. Castillo
## Es muy probable que exista en algún lado un reporte acerca de este código

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos expermentales
steps = np.arange(0, 2100, 100)  # Marcamos cada 100 pasos
measurements = np.array(
    [9.64, 9.46, 9.27, 9.06, 8.88, 8.67, 8.5, 8.29, 8.12, 7.96, 7.76, 7.57, 7.36, 7.16, 6.94, 6.75, 6.56, 6.37, 6.17,
     5.97, 5.79])  # distancias medidas
diference = -1 * (np.round(np.diff(measurements),2))  # Diferencia entre cada medición

# Sacamos estadísticas
mean_value = np.mean(diference)
std_deviation = np.std(diference)
variance_value = np.var(diference)

single_step_mean_distance = (mean_value) / 100
single_step_std_deviation = (std_deviation) / 100
single_step_variance_value = (variance_value) / 10000

# Ajustamos una función linear a los datos
slope, intercept, r_value, p_value, std_err = linregress(steps, measurements)

# Función lineal _mx + b_
fit_line = slope * steps + intercept

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(steps, measurements, 'bo', label='Measurements', markersize=5)  # Scatter plot
plt.plot(steps, fit_line, 'r-', label=f'Fit: y={slope:.2f}x + {intercept:.2f}', linewidth=2)  # Ajuste lineal

# Etiquetas
plt.xlabel('Pasos')
plt.ylabel('Distancia (cm)')
plt.title('Distancia (cm) contra Pasos')
plt.legend()



# Gráfica barra
plt.figure(figsize=(10,6))
etiquetas_de_medición = [f"{i+1}" for i in range(len(diference))]
plt.bar(etiquetas_de_medición, diference, color='skyblue', edgecolor='black')

# Add titles and labels for the bar chart
plt.title('Mediciones')
plt.xlabel('Mediciones')
plt.ylabel('cm')

plt.axhline(mean_value, color='red', linestyle='--', label=f'Promedio: {mean_value:.4f} cm')
plt.legend(

)
# Show values on top of the bars
for index, value in enumerate(diference):
    plt.text(index, value, str(value), ha='center', va='bottom')

plt.grid(axis='y', alpha=0.75)

# Dividiendo la impresión en líneas más cortas
print(f"Las mediciones tomadas fueron:")
line_length = 5
for i in range(0, len(diference), line_length):
    print(' cm , '.join(map(str, diference[i:i+line_length])) + ' cm')

print(f"La distancia promedio recorrida es {mean_value:.4f} cm")
print(f"La desviación estandar es {std_deviation:.4f} cm")
print(f"La varianza es {variance_value:.4f} cm")
print(f"La distancia promedio recorrida en un solo paso es {single_step_mean_distance:.4f} cm")



plt.show()
