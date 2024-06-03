# -*- coding: utf-8 -*-

from pyomo.environ import *

# Crear un modelo
model = ConcreteModel()

# Conjuntos
model.i = Set(initialize=['o1', 'o2', 'o3'])
model.j = Set(initialize=['d1', 'd2', 'd3', 'd4'])

# Parámetros
model.oferta = Param(model.i, initialize={'o1': 300, 'o2': 500, 'o3': 200})
model.demanda = Param(model.j, initialize={'d1': 200, 'd2': 300, 'd3': 100, 'd4': 400})

# Tabla de costos
costos_dict = {('o1', 'd1'): 8, ('o1', 'd2'): 6, ('o1', 'd3'): 10, ('o1', 'd4'): 9,
               ('o2', 'd1'): 9, ('o2', 'd2'): 12, ('o2', 'd3'): 13, ('o2', 'd4'): 7,
               ('o3', 'd1'): 14, ('o3', 'd2'): 9, ('o3', 'd3'): 16, ('o3', 'd4'): 5}
model.costos = Param(model.i, model.j, initialize=costos_dict)

# Variables
model.x = Var(model.i, model.j, within=NonNegativeReals)

# Función objetivo
def objective_function(model):
    return sum(model.x[i, j]*model.costos[i, j] for i in model.i for j in model.j)
model.objectiveFunction = Objective(rule=objective_function, sense=minimize)

# Restricciones
def restriccion_oferta(model, i):
    return sum(model.x[i, j] for j in model.j) <= model.oferta[i]
model.restriccionOferta = Constraint(model.i, rule=restriccion_oferta)

def restriccion_demanda(model, j):
    return sum(model.x[i, j] for i in model.i) == model.demanda[j]
model.restriccionDemanda = Constraint(model.j, rule=restriccion_demanda)

# Resolver el modelo
solver = SolverFactory('glpk')
solver.solve(model)

# Mostrar los resultados
print('Relación Origen - Destino: ')
for i in model.i:
    for j in model.j:
        print('x[', i, ',', j, '] = ', model.x[i, j].value)
print('Costo total: ', model.objectiveFunction())
