Sets
    i Origen (filas) /o1, o2, o3/
    j  Destino (columnas) /d1, d2, d3, d4/;

Parameters
    oferta(i) /o1 300, o2 500, o3 200/
    demanda(j) /d1 200, d2 300, d3 100, d4 400/;
    
Table costos(i, j)
    d1  d2  d3  d4
o1   8   6   10  9
o2   9   12  13  7
o3   14  9   16  5;

Positive Variables
    x(i, j);

Variables
    z;
    
Equations
    objectiveFunction
    restriccionOferta(i)
    restriccionDemanda(j);

objectiveFunction           ..  z=e= sum((i, j), x(i, j)*costos(i, j));
restriccionOferta(i)        ..  sum(j, x(i, j)) =l= oferta(i);
restriccionDemanda(j)       ..  sum(i, x(i, j)) =e= demanda(j);

Model model1 /all/ ;
option mip=cplex;
Solve model1 using lp minimizing z;

Display 'Relación Origen - Destino: ', X.l;
Display 'Costo total: ', z.l;
