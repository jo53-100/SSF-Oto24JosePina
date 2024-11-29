# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:04:29 2024

@author: luish
"""
import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros físicos del sistema
g = 9.81  # gravedad, en m/s^2
L = 1.0   # longitud del péndulo, en metros
b = 0.05  # coeficiente de amortiguamiento
beta = 0.1 # amplitud del término de forzamiento
omega = 1.0 # frecuencia del término de forzamiento

# Valores de k para comparar
k_values = [50, 75, 99]  # tres valores de k

# Definir la función de derivadas (ecuaciones diferenciales)
def pendulum_def(state, time, k):
    theta, omega_dot = state  # theta = ángulo, omega_dot = velocidad angular
    dtheta_dt = omega_dot
    domega_dt = -(g / L) * np.sin(theta) - b * omega_dot - k * theta + beta * np.cos(omega * time)  # Término -k * theta
    return [dtheta_dt, domega_dt]

# Condiciones iniciales
theta_0 = np.pi / 4  # ángulo inicial (45 grados)
omega_dot_0 = 0.0    # velocidad angular inicial
state_0 = [theta_0, omega_dot_0]

# Intervalo de tiempo
time = np.linspace(0, 10, 1000)

plt.figure(figsize=(10, 5))

# Resolver y graficar para cada valor de k
for k in k_values:
    # Resolver las ecuaciones diferenciales
    solution = odeint(pendulum_def, state_0, time, args=(k,))
    
    # Extraer las soluciones para theta y omega_dot
    theta_sol = solution[:, 0]
    omega_dot_sol = solution[:, 1]
    
    # Graficar los resultados
    plt.plot(time, theta_sol, label=f'θ (k={k})')
    plt.plot(time, omega_dot_sol, label=f'ω_dot (k={k})', linestyle='--')

# Personalizar la gráfica
plt.title('Péndulo Amortiguado Forzado con Diferentes k')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo / Velocidad angular')
plt.legend()
plt.grid(True)
plt.show()
