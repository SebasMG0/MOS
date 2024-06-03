Sets
    i Técnica (filas) /S, NS, DL, RL/
    j  Científicos (columnas) /c1*c6/;
    
Table relacionesTC(i, j)
    c1  c2  c3  c4  c5  c6
S   85  88  87  82  91  68
NS  78  77  77  76  79  78
DL  82  81  82  80  86  81
RL  84  84  88  83  84  85
;
  
Variables z Función objetivo;
Binary Variable X(i, j) Determina la relación Técnica-Científico;
Equations
    objectiveFunction
    unicidadTecnica (i)
    unicidadCientifico(j);
    
objectiveFunction              ..  z =e= sum((i,j), X(i,j)*relacionesTC(i, j));
unicidadTecnica (i)            ..  sum(j, X(i, j)) =e= 1;
unicidadCientifico(j)          ..  sum(i, X(i, j)) =l= 1;


Model model1 /all/ ;
option mip=cplex
Solve model1 using mip maximizing z;

Display 'Relación Técnica - Científico: ', X.l;
Display 'Puntos totales: ', z.l;
