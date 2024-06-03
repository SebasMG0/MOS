from random import randint

of= (3, 2) # Función Objetivo
r= [(2, 1, 100), #Restricciones
    (1, 1, 80), 
    (1, 0, 40)]

fevs= [(0, 0), (0, 80), (20, 60), (40, 0), (40, 20)]

def buildGraph(fevs:list=fevs, r:list=r):
    g= [[False]*len(r) for _ in range(len(fevs))]
    
    for i in range(len(r)):
        for j in range(1, len(fevs)):
            if fevs[j][0]*r[i][0]+ fevs[j][1]*r[i][1] == r[i][2]:
                g[j][i]=True
    return g

def evalOf(of:tuple, p:tuple):
    return of[0]*p[0]+of[1]*p[1]

def getAdjs(g, init, fevs):
    
    if init == 0: return( [i for i, f in enumerate(fevs[1:]) if f[0]==0 or f[1]==0])
    
    adj= []
    if g[init][0]==0 or g[init][1]==0: adj.append(0)
    
    for j in range(len(g[init])):
        if g[init][j]:
            for i in range(len(g)):
                if g[i][j] and i!=init:
                    adj.append(i)
    return adj
            
def simplex(fevs:list, g:list, of:tuple):
    init= randint(0, len(g)-1)
    value= evalOf(of, fevs[init])
    
    while init>-1:
        adjs= getAdjs(g, init, fevs)
        valueOfAdjs= [evalOf(of, fevs[i]) for i in adjs]
        maxValue= max(value, max(valueOfAdjs))
        if maxValue == value: return fevs[init], value
        
        value= maxValue
        init= adjs[valueOfAdjs.index(value)]
        
    return fevs[init], value

value= simplex(fevs, buildGraph(), of)
print(f"- Punto optimo: {value[0]}\n- Valor máximo de la función: {value[1]}" )