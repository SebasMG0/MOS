import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff

# Definición de la función y sus derivadas
x = symbols('x')
f = 3*x**3 - 10*x**2 - 56*x + 50
f_prime = diff(f, x) # Primera derivada
f_dprime = diff(f_prime, x) # Segunda derivada

# Parámetros
alpha = 0.6
k = 0 # Punto de arranque
convergencia = 0.001
iteraciones = []

# Método de Newton-Raphson
while abs(f_prime.evalf(subs={x:k})) > convergencia:
    l = k - (alpha * (f_prime.evalf(subs={x:k}) / f_dprime.evalf(subs={x:k})))
    k = l
    iteraciones.append(k)

# Imprimir el mínimo/máximo encontrado
print("Coordenada X: ", k)
print("Coordenada Y (Mínimo): ", f.evalf(subs={x:k}))

# Graficar la función
x_vals = np.linspace(-6, 6, 400)
y_vals = [f.evalf(subs={x: val}) for val in x_vals]
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='y = 3x^3 - 10x^2 - 56x + 50')

# Graficar el mínimo/máximo encontrado
plt.plot(k, f.evalf(subs={x:k}), 'ro')
plt.text(k, f.evalf(subs={x:k}), '  Min/Max', verticalalignment='bottom')

# Graficar los puntos de cada iteración
for i, val in enumerate(iteraciones):
    plt.plot(val, f.evalf(subs={x:val}), 'go')
    plt.text(val, f.evalf(subs={x:val}), f'P{i+1}', verticalalignment='top')

plt.legend()
plt.grid(True)
plt.show()
