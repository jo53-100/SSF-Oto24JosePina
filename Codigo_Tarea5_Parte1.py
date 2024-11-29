
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
N = 1000  # número de pasos a tomar
xo = 0.0  # posición inicial (en reposo)
vo = 0.0  # velocidad inicial
tau = 3.0  # tiempo total de simulación en segundos
dt = tau / float(N - 1)  # paso de tiempo
k = 3.5  # constante del resorte en N/m
m = 0.2  # masa en kg
gravity = 9.8  # gravedad en m/s²

# Tiempo para la gráfica
time = np.linspace(0, tau, N)

# Inicializar el arreglo para guardar resultados
y = np.zeros((N, 2))  # N x 2 array
y[0, 0] = xo  # establecer estado inicial
y[0, 1] = vo

# Definir la función que calcula las derivadas
def SHO(state, time):
    g0 = state[1]  # dx/dt = v
    g1 = -k/m * state[0] - gravity  # dv/dt = -k/m * x - g
    return np.array([g0, g1])

# Método de Euler para resolver las EDOs
for j in range(N - 1):
    y[j + 1] = y[j] + dt * SHO(y[j], time[j])

# Extraer datos de posición y velocidad
xdata = [y[j, 0] for j in range(N)]
vdata = [y[j, 1] for j in range(N)]

# Graficar los resultados
plt.plot(time, xdata, label="Posición (x)")
plt.plot(time, vdata, label="Velocidad (v)", linestyle='--')
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición / Velocidad")
plt.title("Oscilador Armónico Simple")
plt.legend()
plt.grid(True)
plt.show()


