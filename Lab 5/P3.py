from sympy import symbols, hessian, Function, N, sqrt, Matrix
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sympy import lambdify

# Variables como símbolos
x, y = symbols('x y')

# Parámetros
alpha= 1
convergencia= 0.001
i, j= 0, 10

# Funciones
f = (x-1)**2 + 100*(y-x**2)**2
gradiente = [f.diff(var) for var in (x, y)]
hessiano = hessian(f, (x, y))
norma = sqrt(sum([g**2 for g in gradiente]))


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

x_range, y_range = np.meshgrid(np.linspace(-6, 6, 100), np.linspace(-10, 10, 100))


f_lambdified = lambdify((x, y), f, "numpy")
z_range = f_lambdified(x_range, y_range)

ax.plot_surface(x_range, y_range, z_range, cmap='viridis')

x_values, y_values, z_values= [], [], []
while sqrt(sum([k**2 for k in [N(g.subs({x:i, y:j})) for g in gradiente]])) > convergencia:
    inversa = Matrix(hessiano.subs({x:i, y:j})).inv()
    j = i - alpha * (inversa * Matrix([N(g.subs({x:i, y:j})) for g in gradiente]))[0]
    i = j
    x_values.append(i)
    y_values.append(j)
    z_values.append(f.subs({x:i, y:j}))

ax.scatter(x_values[:-1], y_values[:-1], z_values[:-1], color='c')
ax.scatter([x_values[-1]], [y_values[-1]], [z_values[-1]], color='r', s=150)
ax.view_init(30, 60)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


print(f'X: {x_values[-1]}')
print(f'Y: {y_values[-1]}')
print(f'Z: {z_values[-1]}')

plt.show()
