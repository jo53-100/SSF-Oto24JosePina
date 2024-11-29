## T6 Reproduccion de unas cosillas de un .ipynb

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


## «Implemente la función representativa del sistema en lenguaje Python.
## Tenga en cuenta que la variable de estado sería un ndArray de 3 dimensiones.
## Por otra parte, la función recibe los parámetros de entrada σ , ρ y β».

def solve_lorenz(state, t, σ, ρ, β):
    x, y, z = state

    dx = σ * (y - x)
    dy = x * (ρ - z) - y
    dz = (x * y) - (β * z)
    return dx, dy, dz


# Ejemplo resolviendo para ciertas condiciones iniciales
print(solve_lorenz((1, 1, 1), t=1, σ=10, ρ=28, β=8 / 3))

# «Escriba el código correspondiente a la simulación de este sistema para un intervalo de tiempo t∈[0,100]
# que contenga 3000 valores equidistantes.
# Además, utilice los parámetros σ=10, ρ=28, β=8/3 y el vector de condiciones iniciales (1,1,1).
# Emplee para ello la función odeint».

initial_state = (1., 1., 1.)
σ, ρ, β = 10, 28, 8 / 3

t = np.linspace(0, 100, 3000)

print('Valores equidistantes de t:', t.size)

states = odeint(solve_lorenz, initial_state, t, args=(σ, ρ, β))

xs = states[:, 0]
ys = states[:, 1]
zs = states[:, 2]

ax = plt.figure().add_subplot(projection='3d')
ax.plot(xs, ys, zs, lw=0.5, c='#7B86B2')
ax.set_title("Lorenz Attractor with odeint")
plt.show()

# «Cree una gráfica en 3 dimensiones que utilice la paleta de colores llamada plt.cm.plasma
# para representar la solución la cual deberá de tener una forma similar a la Figura 1».

cmap = plt.cm.plasma
print("Tipo del objeto colormap:", type(cmap))
# Los colores pueden ser accedidos directamente por indexación
print("Elemento indexado:", cmap(0))


def lorenz_attractor(state0, parameters, ax=None, text_offset=0.01):
    σ, ρ, β = parameters
    n = 3000
    t = np.linspace(0, 100, n)

    # Resolvemos las ecuaciones para la secuencia de puntos t
    states = odeint(solve_lorenz, state0, t, args=(σ, ρ, β))
    xs = states[:, 0]
    ys = states[:, 1]
    zs = states[:, 2]

    if ax is None:
        ax = plt.figure(figsize=(7, 8)).add_subplot(projection='3d')

    # Intervalos de 10 unidades de ancho
    s = 10

    # Iteramos en estos intervalos aplicando el colormap correspondiente
    for i in range(0, n - s, s):
        ax.plot(xs[i:i + s + 1], ys[i:i + s + 1], zs[i:i + s + 1], color=cmap(i / n), alpha=0.5, lw=1)

    ax.text2D(0.44, text_offset, f"ρ={ρ}", transform=ax.transAxes)
    ax.figure.tight_layout()
    return ax.figure


# Condiciones iniciales propuestas en la Figura 1
lorenz_attractor((1, 1, 1), (10, 28, 8 / 3))
plt.show()

# «Solucione el mismo problema con los mismos parámetros a excepción de ρ,
# el cual tomará los valores −42, 15, 28 y 100.
# Almacene las respuestas en dos listas, una para el parámetro ρ
# y la otra para la solución correspondiente.».

rho_values = [-42, 15, 28, 100]
solutions = [lorenz_attractor((1, 1, 1), (10, rho, 8/3)) for rho in rho_values]

for solution in solutions:
  solution.show()

# «Cree gráficas de 3 dimensiones para representar cada solución,
# todas en la misma figura. Para ello cree una figura de 2 fila y 2 columnas.
# Coloque en el texto del título de la gráfica el parámetro ρ
# igualado a el valor correspondiente en cada caso. Garantice que la figura tenga un tamaño de 10×10».

rows, cols = 2, 2
size = (10, 10)

# Instanciamos nuestra figura y sus axes
fig, axs = plt.subplots(rows, cols, figsize=size, subplot_kw = dict(projection='3d'))

# Transformamos el array a uno bidimensional de rows×cols
rho_values2d = np.array(rho_values).reshape(rows, cols)

# Iteramos en (0, 0), (0, 1), (1, 0), (1, 1)
for row, col in np.ndindex((rows, cols)):
  rho = rho_values2d[row ,col]
  # Introducimos el eje correspondiente en nuestra función
  lorenz_attractor((1, 1, 1),
                   (10, rho, 8/3),
                   ax=axs[row, col],
                   text_offset=-0.03)

fig.show()

fsize = (15, 15)
ndim = 8

def butterfly(ax, colormap, rho, angle):
  tmax = 100
  n = 10000
  sigma, rho, beta = (10, rho, 2.667)
  u0, v0, w0 = (0, 1, 1.05)
  t = np.linspace(0, tmax, n)

  soln = odeint(solve_lorenz, (u0, v0, w0), t, args=(sigma, rho, beta))
  # Interpolate solution onto the time grid, t.
  x, y, z = soln[:, 0], soln[:, 1], soln[:, 2]

  ax.set_facecolor('k')

  s = 10
  cmap = getattr(plt.cm, colormap)
  for i in range(0,n-s,s):
      ax.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=cmap(i/n), alpha=0.4)

  # Remove all the axis clutter, leaving just the curve.
  ax.set_axis_off()
  ax.view_init(angle, angle)

axs = plt.figure(facecolor='k', figsize=fsize).subplots(ndim, ndim, subplot_kw = dict(projection='3d'))

for i, (row, col) in enumerate(np.ndindex((ndim, ndim))):
  butterfly(axs[row, col], plt.colormaps()[i], rho=2.5*i, angle=10*i)