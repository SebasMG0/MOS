import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, solve

# Definición de la función y sus derivadas
x = symbols('x')
f = x**5 - 8*x**3 + 10*x + 6
f_prime = diff(f, x) # Primera derivada
f_dprime = diff(f_prime, x) # Segunda derivada

# Parámetros
alpha = 0.6
convergencia = 0.001
iteraciones = []

# Encuentra los puntos críticos de la función
critical_points = solve(f_prime, x)

# Método de Newton-Raphson para cada punto crítico
min_max_points = []
for k in critical_points:
    while abs(f_prime.evalf(subs={x:k})) > convergencia:
        l = k - (alpha * (f_prime.evalf(subs={x:k}) / f_dprime.evalf(subs={x:k})))
        k = l
    min_max_points.append(k)

# Imprimir los mínimos/máximos encontrados
for point in min_max_points:
    print("Coordenada X: ", point)
    print("Coordenada Y (Mínimo/Máximo): ", f.evalf(subs={x:point}))
    print("\n")

# Graficar la función
x_vals = np.linspace(-3, 3, 400)
y_vals = [f.evalf(subs={x: val}) for val in x_vals]
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='y = x^5 - 8x^3 + 10x + 6')

# Graficar los mínimos/máximos encontrados
for point in min_max_points:
    plt.plot(point, f.evalf(subs={x:point}), 'ko')

# Graficar el mínimo/máximo global
global_min_max = min(min_max_points, key=lambda point: f.evalf(subs={x:point}))
plt.plot(global_min_max, f.evalf(subs={x:global_min_max}), 'ro')

plt.legend()
plt.grid(True)
plt.show()
