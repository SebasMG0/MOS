# -*- coding: utf-8 -*-

from pyomo.environ import *
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Crear un modelo concreto
model = ConcreteModel()

# Conjuntos
model.i = Set(initialize=['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'])
model.j = Set(initialize=model.i)
model.k = Set(initialize=['x', 'y'])

# Tabla de coordenadas
c_dict = {
    ('n1', 'x'): 20, ('n1', 'y'): 6,
    ('n2', 'x'): 22, ('n2', 'y'): 1,
    ('n3', 'x'): 9, ('n3', 'y'): 2,
    ('n4', 'x'): 3, ('n4', 'y'): 25,
    ('n5', 'x'): 21, ('n5', 'y'): 10,
    ('n6', 'x'): 29, ('n6', 'y'): 2,
    ('n7', 'x'): 14, ('n7', 'y'): 12
}
model.c = Param(model.i, model.k, initialize=c_dict)

# Parámetro d
d_dict = {(i, j): math.sqrt((model.c[i, 'x'] - model.c[j, 'x'])**2 + (model.c[i, 'y'] - model.c[j, 'y'])**2) for i in model.i for j in model.j}
for i in model.i:
    for j in model.j:
        if d_dict[i, j] > 20 or i == j:
            d_dict[i, j] = 999
model.d = Param(model.i, model.j, within=Any, initialize=d_dict)

# Vértice inicial y final
model.vo = 'n4'
model.vf = 'n6'

# Variables
model.x = Var(model.i, model.j, within=Binary)
model.z = Var()

#Gráfica
plt.plot([c_dict[node, 'x'] for node in model.i], [c_dict[node, 'y'] for node in model.j], 'ko')

# Función objetivo
def objective_function(model):
    return sum(model.d[i, j] * model.x[i, j] for i in model.i for j in model.j)
model.objectiveFunction = Objective(rule=objective_function, sense=minimize)

# Restricciones
def source_node(model, i):
    if i == model.vo:
        return sum(model.x[i, j] for j in model.j) == 1
    else:
        return Constraint.Skip
model.sourceNode = Constraint(model.i, rule=source_node)

def destination_node(model, j):
    if j == model.vf:
        return sum(model.x[i, j] for i in model.i) == 1
    else:
        return Constraint.Skip
model.destinationNode = Constraint(model.j, rule=destination_node)

def intermediate_node(model, i):
    if i != model.vo and i != model.vf:
        return sum(model.x[i, j] for j in model.j) - sum(model.x[j, i] for j in model.j) == 0
    else:
        return Constraint.Skip
model.intermediateNode = Constraint(model.i, rule=intermediate_node)

# Resolver el modelo
solver = SolverFactory('glpk')
solver.solve(model)

# Mostrar los resultados
x, y= [],[]
print('Distancias calculadas: ')
for i in model.i:
    plt.text(c_dict[i, 'x']+0.3, c_dict[i, 'y']+0.4, i)  # Añade el texto al gráfico
    for j in model.j:
        print('d[', i, ',', j, '] = ', model.d[i, j])
        if model.d[i, j]<=20:
            x.append(c_dict[i, 'x'])
            x.append(c_dict[j, 'x'])
            
            y.append(c_dict[i, 'y'])
            y.append(c_dict[j, 'y'])
plt.plot(x, y, 'k--')

print('\nNodos seleccionados: ')
x, y= [],[]
for i in model.i:
    for j in model.j:
        if model.x[i, j].value>0:
            x.append(c_dict[i, 'x'])
            x.append(c_dict[j, 'x'])
            
            y.append(c_dict[i, 'y'])
            y.append(c_dict[j, 'y'])
            print('x[', i, ',', j, '] = ', model.x[i, j].value)

print('\nDistancia Total: ', model.objectiveFunction())
plt.plot(x, y, 'r--')
plt.show()


