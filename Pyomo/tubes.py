# -*- coding: utf-8 -*-

from pyomo.environ import *

# Crear un modelo concreto
model = ConcreteModel()

# Conjuntos
model.i = Set(initialize=['t1', 't2', 't3', 't4', 't5', 't6', 't7'])
model.j = Set(initialize=['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12', 'l13', 'l14', 'l15', 'l16', 'l17', 'l18', 'l19', 'l20'])

# Tabla de relaciones
relaciones_dict = {
    ('t1', 'l1'): 1, ('t1', 'l2'): 0, ('t1', 'l3'): 0, ('t1', 'l4'): 0, ('t1', 'l5'): 1, ('t1', 'l6'): 0, ('t1', 'l7'): 0, ('t1', 'l8'): 0, ('t1', 'l9'): 0, ('t1', 'l10'): 0, ('t1', 'l11'): 0, ('t1', 'l12'): 0, ('t1', 'l13'): 0, ('t1', 'l14'): 0, ('t1', 'l15'): 0, ('t1', 'l16'): 0, ('t1', 'l17'): 0, ('t1', 'l18'): 0, ('t1', 'l19'): 0, ('t1', 'l20'): 0,
    ('t2', 'l1'): 0, ('t2', 'l2'): 1, ('t2', 'l3'): 1, ('t2', 'l4'): 0, ('t2', 'l5'): 0, ('t2', 'l6'): 1, ('t2', 'l7'): 1, ('t2', 'l8'): 0, ('t2', 'l9'): 0, ('t2', 'l10'): 0, ('t2', 'l11'): 0, ('t2', 'l12'): 0, ('t2', 'l13'): 0, ('t2', 'l14'): 0, ('t2', 'l15'): 0, ('t2', 'l16'): 0, ('t2', 'l17'): 0, ('t2', 'l18'): 0, ('t2', 'l19'): 0, ('t2', 'l20'): 0,
    ('t3', 'l1'): 0, ('t3', 'l2'): 0, ('t3', 'l3'): 0, ('t3', 'l4'): 0, ('t3', 'l5'): 1, ('t3', 'l6'): 0, ('t3', 'l7'): 0, ('t3', 'l8'): 0, ('t3', 'l9'): 1, ('t3', 'l10'): 0, ('t3', 'l11'): 0, ('t3', 'l12'): 0, ('t3', 'l13'): 0, ('t3', 'l14'): 0, ('t3', 'l15'): 0, ('t3', 'l16'): 0, ('t3', 'l17'): 0, ('t3', 'l18'): 0, ('t3', 'l19'): 0, ('t3', 'l20'): 0,
    ('t4', 'l1'): 0, ('t4', 'l2'): 0, ('t4', 'l3'): 0, ('t4', 'l4'): 0, ('t4', 'l5'): 0, ('t4', 'l6'): 0, ('t4', 'l7'): 0, ('t4', 'l8'): 1, ('t4', 'l9'): 0, ('t4', 'l10'): 0, ('t4', 'l11'): 0, ('t4', 'l12'): 1, ('t4', 'l13'): 0, ('t4', 'l14'): 0, ('t4', 'l15'): 0, ('t4', 'l16'): 1, ('t4', 'l17'): 0, ('t4', 'l18'): 0, ('t4', 'l19'): 1, ('t4', 'l20'): 1,
    ('t5', 'l1'): 0, ('t5', 'l2'): 0, ('t5', 'l3'): 0, ('t5', 'l4'): 0, ('t5', 'l5'): 0, ('t5', 'l6'): 0, ('t5', 'l7'): 0, ('t5', 'l8'): 0, ('t5', 'l9'): 1, ('t5', 'l10'): 1, ('t5', 'l11'): 0, ('t5', 'l12'): 0, ('t5', 'l13'): 1, ('t5', 'l14'): 1, ('t5', 'l15'): 0, ('t5', 'l16'): 0, ('t5', 'l17'): 0, ('t5', 'l18'): 0, ('t5', 'l19'): 0, ('t5', 'l20'): 0,
    ('t6', 'l1'): 0, ('t6', 'l2'): 0, ('t6', 'l3'): 0, ('t6', 'l4'): 0, ('t6', 'l5'): 0, ('t6', 'l6'): 0, ('t6', 'l7'): 0, ('t6', 'l8'): 0, ('t6', 'l9'): 0, ('t6', 'l10'): 1, ('t6', 'l11'): 1, ('t6', 'l12'): 0, ('t6', 'l13'): 0, ('t6', 'l14'): 1, ('t6', 'l15'): 1, ('t6', 'l16'): 0, ('t6', 'l17'): 0, ('t6', 'l18'): 0, ('t6', 'l19'): 0, ('t6', 'l20'): 0,
    ('t7', 'l1'): 0, ('t7', 'l2'): 0, ('t7', 'l3'): 0, ('t7', 'l4'): 0, ('t7', 'l5'): 0, ('t7', 'l6'): 0, ('t7', 'l7'): 0, ('t7', 'l8'): 0, ('t7', 'l9'): 0, ('t7', 'l10'): 0, ('t7', 'l11'): 0, ('t7', 'l12'): 0, ('t7', 'l13'): 1, ('t7', 'l14'): 0, ('t7', 'l15'): 0, ('t7', 'l16'): 0, ('t7', 'l17'): 1, ('t7', 'l18'): 0, ('t7', 'l19'): 0, ('t7', 'l20'): 0
}
model.relaciones = Param(model.i, model.j, initialize=relaciones_dict)

# Variables
model.x = Var(model.j, within=Binary)
model.z = Var()

# Función objetivo
def objective_function(model):
    return sum(model.x[j] for j in model.j)
model.objectiveFunction = Objective(rule=objective_function, sense=minimize)

# Restricciones
def cobertura_total(model, i):
    return sum(model.x[j]*model.relaciones[i, j] for j in model.j) >= 1
model.coberturaTotal = Constraint(model.i, rule=cobertura_total)

# Resolver el modelo
solver = SolverFactory('glpk')
solver.solve(model)

# Mostrar los resultados
print('Lozas a levantar: ')
for j in model.j:
    if model.x[j].value==1:
        print('x[', j, '] = ', model.x[j].value) 
print('Mínimo de lozas a levantar: ', model.objectiveFunction())
