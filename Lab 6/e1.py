# Importaciones necesarias
from pyomo.environ import *

# Configuración de Epsilon----------------------------------------------------
epsilons = [5, 4, 3, 2]  # Valores de epsilon a iterar

# Creación del Modelo---------------------------------------------------------
Model = ConcreteModel()

# Sets & Parámetros-----------------------------------------------------------
numNodes = 5
Model.N = RangeSet(1, numNodes)

# Hops------------------------------------------------------------------------
Model.h = Param(Model.N, Model.N, mutable=True, initialize=999)
Model.h[1, 2] = 1
Model.h[1, 3] = 1
# ... (resto de inicialización de hops)

# Costos----------------------------------------------------------------------
Model.c = Param(Model.N, Model.N, mutable=True, initialize=999)
Model.c[1, 2] = 10
Model.c[1, 3] = 5
# ... (resto de inicialización de costos)

# Origen y Destino------------------------------------------------------------
s = 1
d = 5

# Variables-------------------------------------------------------------------
Model.x = Var(Model.N, Model.N, domain=Binary)

# Funciones Objetivo----------------------------------------------------------
Model.f1 = sum(Model.x[i, j] * Model.h[i, j] for i in Model.N for j in Model.N)
Model.f2 = sum(Model.x[i, j] * Model.c[i, j] for i in Model.N for j in Model.N)


# Proceso para ejecutar el modelo matemático con el método eConstraint--------
f1_vec = []
f2_vec = []

for epsilon in epsilons:
    # Restricción de eConstraint para f2
    Model.eConstraint = Constraint(expr=Model.f2 <= epsilon)
    
    # Función objetivo general (minimizar f1)
    Model.O_f1 = Objective(expr=Model.f1, sense=minimize)
    
    # Resolución del modelo
    SolverFactory('glpk').solve(Model)
    
    # Almacenamiento de resultados
    valorF1 = value(Model.f1)
    valorF2 = value(Model.f2)
    f1_vec.append(valorF1)
    f2_vec.append(valorF2)
    
    # Eliminación de la restricción eConstraint para la siguiente iteración
    Model.del_component('eConstraint')

