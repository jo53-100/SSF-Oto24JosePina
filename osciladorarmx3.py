## T4 sim de sist fisicos
## commit test
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def nonlinear_oscillator(state, omega, beta):
    x, v = state
    dxdt = v
    dvdt = -omega ** 2 * x - beta * x ** 3
    return [dxdt, dvdt]


# Parámetros
omega = 1.0  # frecuencia natural
beta = 1.41  # coeficiente de no linealidad
t = np.linspace(0, 20, 1000)  # Intervalo de tiempo

# Condiciones iniciales
x0 = 2.0  # posición inicial
v0 = 0.0  # velocidad incial
state0 = [x0, v0]

# Resuelve EDO
solution = odeint(nonlinear_oscillator, state0, t, args=(omega, beta))
x = solution[:, 0]  # position
v = solution[:, 1]  # velocity

# Creamos figura con dos gráficos
plt.figure(figsize=(12, 5))

# Posición vs Tiempo
plt.subplot(121)
plt.plot(t, x, 'b-', label=f'No lineal (β={beta})')
# For comparison, plot linear case (β=0)
solution_linear = odeint(nonlinear_oscillator, state0, t, args=(omega, 0))
plt.plot(t, solution_linear[:, 0], 'r--', label='Linear (β=0)')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Posición vs Tiempo')
plt.grid(True)
plt.legend()

# Phase space plot
plt.subplot(122)
plt.plot(x, v, 'b-', label='No lineal')
plt.plot(solution_linear[:, 0], solution_linear[:, 1], 'r--', label='Lineal')
plt.xlabel('Posición')
plt.ylabel('Velocidad')
plt.title('Espacio de fase')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Print some key observations
max_amplitude_nonlinear = np.max(np.abs(x))
max_amplitude_linear = np.max(np.abs(solution_linear[:, 0]))
print(f"Amplitud máxima (no lineal): {max_amplitude_nonlinear:.2f}")
print(f"Amplitud máxima (lineal): {max_amplitude_linear:.2f}")
