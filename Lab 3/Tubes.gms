Sets
    i Tubos (De izquierda a derecha) /t1*t7/
    j  Lozas (Enumeradas de izquierda a derecha) /l1*l20/;
    
Table relaciones(i, j)
    l1  l2  l3  l4  l5  l6  l7  l8  l9  l10 l11 l12 l13 l14 l15 l16 l17 l18 l19 l20
t1  1   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
t2  0   1   1   0   0   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0
t3  0   0   0   0   1   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0
t4  0   0   0   0   0   0   0   1   0   0   0   1   0   0   0   1   0   0   1   1
t5  0   0   0   0   0   0   0   0   1   1   0   0   1   1   0   0   0   0   0   0
t6  0   0   0   0   0   0   0   0   0   1   1   0   0   1   1   0   0   0   0   0
t7  0   0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   1   0   0   0;
  
Variables z;
Binary Variable x(j);
Equations
    objectiveFunction,
    coberturaTotal (i);
    
objectiveFunction              ..  z =e= sum(j, x(j));
coberturaTotal (i)            ..  sum(j, x(j)*relaciones(i, j)) =g= 1;


Model model1 /all/ ;
option mip=cplex
Solve model1 using mip minimizing z;

Display 'Lozas a levantar', X.l;
Display 'Mínimo de lozas a levantar: ', z.l;
