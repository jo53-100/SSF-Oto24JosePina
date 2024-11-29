##T5pt2 simsist
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
N = 1000  # número de pasos a tomar
xo = 0.0  # posición inicial
vo = 0.0  # velocidad inicial
tau = 10.0  # tiempo total de simulación en segundos
dt = tau / float(N - 1)  # paso de tiempo
m = 0.2  # masa en kg
gravity = 9.8  # gravedad en m/s²


# Función para el método de Runge-Kutta de segundo orden (RK2)
def rk2(y, time, dt, derivs):
    k0 = dt * derivs(y, time)
    k1 = dt * derivs(y + k0, time + dt)
    y_next = y + 0.5 * (k0 + k1)
    return y_next


# Función que define las derivadas
def SHO(state, time):
    g0 = state[1]  # dx/dt = v
    g1 = -k / m * state[0] - gravity  # dv/dt = -k/m * x - g
    return np.array([g0, g1])


# Comparar diferentes valores de k
k_values = [1, 5 , 8]  # tres valores de k
plt.figure(figsize=(10, 6))

# Colores y estilos predefinidos para una mejor visualización
colors = plt.cm.viridis(np.linspace(0, 1, len(k_values)))

for idx, k  in enumerate(k_values):
    # Inicializar el arreglo para guardar resultados
    y_euler = np.zeros((N, 2))
    y_rk2 = np.zeros((N, 2))
    y_euler[0, 0] = xo
    y_euler[0, 1] = vo
    y_rk2[0, 0] = xo
    y_rk2[0, 1] = vo

    # Método de Euler
    for j in range(N - 1):
        y_euler[j + 1] = y_euler[j] + dt * SHO(y_euler[j], j * dt)

    # Método de Runge-Kutta (RK2)
    for j in range(N - 1):
        y_rk2[j + 1] = rk2(y_rk2[j], j * dt, dt, SHO)

    # Graficar resultados
    plt.plot(
        np.linspace(0, tau, N), y_euler[:, 0],
        label=f"Euler (k={k})",
        linestyle='--',
        linewidth=1.5,
        color=colors[idx]
    )

    plt.plot(
        np.linspace(0, tau, N), y_rk2[:, 0],
        label=f"RK2 (k={k})",
        linestyle='-',
        linewidth=2.0,
        color=colors[idx],
    )
plt.yscale('symlog', linthresh=10)
# Etiquetas y título
plt.title("Comparación entre Euler y RK2 para Diferentes k", fontsize=16)
plt.xlabel("Tiempo (s)", fontsize=14)
plt.ylabel("Posición (x)", fontsize=14)
plt.legend(loc='upper right', fontsize=10, frameon=True, shadow=True, ncol=2)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
