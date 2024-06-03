Sets
    i Empleado (filas) /e1, e2, e3, e4/
    j  Tiempo para completar el trabajo (columnas) /t1, t2, t3, t4/;
    
Table trabajos(i, j)
    t1  t2  t3  t4
e1   14  5   8   7
e2   2   12  6   5
e3   7   8   3   9
e4   2   4   6   10;
  
Variables z Función objetivo;
Binary Variable X(i, j) Determina la relación empleado-trabajo;
Equations
    objectiveFunction
    unicidadEmpleado (i)
    unicidadEmpleo (j);
    
objectiveFunction               ..  z =e= sum((i,j), X(i,j)*trabajos(i, j));
unicidadEmpleado (i)            ..  sum(j, X(i, j)) =e= 1;
unicidadEmpleo (j)              ..  sum(i, X(i, j)) =e= 1;

Model model1 /all/ ;
option mip=cplex
Solve model1 using mip minimizing z;

Display 'Relación Empleado - Trabajo: ', X.l;
Display 'Mínimo de horas: ', z.l;