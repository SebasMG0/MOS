Sets
    i Origen (filas) /o1, o2, o3/
    j  Destino (columnas) /d1, d2/;

Parameters
    ofertaKernel(i) /o1 60, o2 80, o3 50/
    demandaKernel(j) /d1 100, d2 90/
    
    ofertaUser(i) /o1 80, o2 50, o3 50/
    demandaUser(j) /d1 60, d2 120/
;

Table costos(i, j)
     d1    d2
o1   300   500 
o2   200   300
o3   600   300
;

Positive Variables
    k(i, j)
    u(i, j);
    

Variables
    z;
    
Equations
    objectiveFunction
    restriccionDemandaKernel(j)
    restriccionDemandaUser(j)
    restriccionOfertaKernel(i)
    restriccionOfertaUser(i)
;

objectiveFunction               ..  z=e= sum((i, j), ( k(i, j)+u(i,j))*costos(i, j) );
restriccionDemandaKernel(j)     ..  sum(i, k(i, j)) =e= demandaKernel(j);
restriccionDemandaUser(j)       ..  sum(i, u(i, j)) =e= demandaUser(j);

restriccionOfertaKernel(i)      ..  sum(j, k(i, j)) =l= ofertaKernel(i);
restriccionOfertaUser(i)        ..  sum(j, u(i, j)) =l= ofertaUser(i);


Model model1 /all/ ;
option mip=cplex;
Solve model1 using lp minimizing z;

Display 'Relación Oferta-Demanda Kernel: ', k.l;
Display 'Relación Oferta-Demanda User: ', u.l;
Display 'Costo total: ', z.l;
