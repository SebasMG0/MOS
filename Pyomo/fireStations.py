# -*- coding: utf-8 -*-

from pyomo.environ import *

# Crear un modelo
model = ConcreteModel()

# Conjuntos
model.i = Set(initialize=['p1', 'p2', 'p3', 'p4', 'p5', 'p6'])
model.j = Set(initialize=model.i)

# Tabla de tiempos
tiempo_dict = {
    ('p1', 'p1'): 0, ('p1', 'p2'): 10, ('p1', 'p3'): 20, ('p1', 'p4'): 30, ('p1', 'p5'): 30, ('p1', 'p6'): 20,
    ('p2', 'p1'): 10, ('p2', 'p2'): 0, ('p2', 'p3'): 25, ('p2', 'p4'): 35, ('p2', 'p5'): 20, ('p2', 'p6'): 10,
    ('p3', 'p1'): 20, ('p3', 'p2'): 25, ('p3', 'p3'): 0, ('p3', 'p4'): 15, ('p3', 'p5'): 30, ('p3', 'p6'): 20,
    ('p4', 'p1'): 30, ('p4', 'p2'): 35, ('p4', 'p3'): 15, ('p4', 'p4'): 0, ('p4', 'p5'): 15, ('p4', 'p6'): 25,
    ('p5', 'p1'): 30, ('p5', 'p2'): 20, ('p5', 'p3'): 30, ('p5', 'p4'): 15, ('p5', 'p5'): 0, ('p5', 'p6'): 14,
    ('p6', 'p1'): 20, ('p6', 'p2'): 10, ('p6', 'p3'): 20, ('p6', 'p4'): 25, ('p6', 'p5'): 14, ('p6', 'p6'): 0
}
model.tiempo = Param(model.i, model.j, initialize=tiempo_dict)

# Parámetro y
model.y = Param(model.i, model.j, initialize={(i, j): 1 if model.tiempo[i, j] <= 15 else 0 for i in model.i for j in model.j})

# Variables
model.x = Var(model.i, within=Binary)
model.z = Var()

# Función objetivo
def objective_function(model):
    return sum(model.x[i] for i in model.i)
model.objectiveFunction = Objective(rule=objective_function, sense=minimize)

# Restricciones
def cobertura_total(model, j):
    return sum(model.x[i]*model.y[i, j] for i in model.i) >= 1
model.coberturaTotal = Constraint(model.j, rule=cobertura_total)

# Resolver el modelo
solver = SolverFactory('glpk')
solver.solve(model)

# Mostrar los resultados
print('-> Pueblos en los que se van a construir estaciones: ')
for i in model.i:
    print('x[', i, '] = ', model.x[i].value)
print('Número de pueblos: ', model.objectiveFunction())


