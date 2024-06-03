Sets
    i /r1*r3/,
    j  /ind, bi, tri /;

Parameters
    r(i) /r1 400, r2 300/,
    b(j) /ind 50, bi 100, tri 200/,
    c(j) /ind 500, bi 700, tri 1000/,
    d(j) /ind 6, bi 4, tri 0/;

Integer Variable x(i, j);
Variable z;
    
Equations
    objectiveFunction,
    capacidadBuses(i),
    limitacionBuses(j);
    
* La función Objetivo pretende minimizar los costos. Por lo que se multiplica el costo de cada bus c(j)
* Por la cantidad de buses que fueron escogidos x(i,j).
objectiveFunction  .. z =e= sum((i, j), c(j)*x(i, j));

* La siguiente restricción se asegura que la demanda de pasajeros sea cumplida, por lo que para cada ruta
* se multiplica la capacidad de cada tipo de bus b(j) por el número de buses escogidos de cada tipo.
* Se suman las capacidades de todos los buses asignados a cada ruta y se verifica que su valor sea mayor
* o igual al requerido para dicha ruta r(i).
capacidadBuses(i)   .. sum(j, b(j)*x(i, j)) =g= r(i);

* Dado que se tienen buses limitados, se espera que el modelo no asigne buses inexistentes.
* Para garantizar lo anterior, la sumatoria de todos los tipos de buses asignados a las rutas no
* debe superar la cantidad de buses que hay para cada tipo d(j).
limitacionBuses(j)  ..  sum(i, x(i,j)) =l= d(j);


Model model1 /all/ ;
option mip=cplex;
Solve model1 using mip minimizing z;

display z.l;
display x.l;
