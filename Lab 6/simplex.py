# of= [-3, -2] # Función objetivo
# vn= set([1, 2]) # Variables no básicas

# # Restricciones: x1 op x2 <= valor
# r= [([2, 1], 100),
#     ([1, 1], 80), 
#     ([1], 40)]

of= [-3, -5] # Función objetivo
vn= set([0, 1]) # Variables no básicas

# Restricciones: x1 op x2 <= valor
# r= [([2, 1], 100),
#     ([1, 1], 80), 
#     ([1], 40)]

r= [([1, 0], 4),
    ([0, 2], 12), 
    ([3, 2], 18)]



# Inicializar la tabla de coeficientes
def formatTable(data= r):
    t= [[0]*(2*len(r)) for _ in range(len(r)+1)]
    
    for i, v in enumerate(data):
        for j, k in enumerate(v[0]):
            t[i][j]= k
        t[i][-1]=v[1]
        t[i][len(r)+i-1]=1
        
    t[-1][0], t[-1][1]= of
    return t

# Prueba de optimidad
def isSolution(data:list):
    for i in data:
        if i < 0: return False
    return True

# Obtener mínimo diferente de cero
def getMin(data:list):
    m, index= data[0], 0
    for i in range(len(data)):
        if data[i]!=0 and abs(data[i])<m:
            m= abs(data[i])
            index= i
    return index, m

def getMax(data:list):
    m, index= data[0], 0
    for i in range(len(data)):
        if abs(data[i])>m:
            m= abs(data[i])
            index= i
    return index, m

def simplex(coor:list):
    t= formatTable()
    print(t)
    var= set(range(len(t[0]))) 
    while not isSolution(t[-1]):
        index, value= getMax(t[-1][:-1]) # Variable no básica con coeficiente más grande
        c= min([(i[-1]/i[index], v) for v, i in enumerate(t[:-1]) if i[index]!=0])
        print(c)
        break
        
        
       
    return None

simplex([])