Sets
    i Tipo de alimento (filas) /c, a, l, p/
    j Valor nutricional (columnas) /cal, prot, az, gra, car/;
    
Table VN(i, j)
            cal     prot    az      gra     car
c           287     26      0       19.3    0
a           204     4.2     0.01    0.5     44.1
l           146     8       13      8       11
p           245     6       25      0.8     55;

Parameters
    k(j) Valor requerido OMS /cal 1500, prot 63, az 25, gra 50, car 200/;
  
Variables
  C     Cantidad de Carne.
  A     Cantidad de Arroz.
  L     Cantidad de Leche.
  P     Cantidad de Pan.
  z     Objective function;

Positive variable C, A, L, P;

Equations
objectiveFunction
mayores (j)
menores (j);

objectiveFunction              ..  z =e= 3000*C + 1000*A + 600*L + 700*P;
mayores (j)  $(ord(j)<= 2)     ..  C*VN('c', j)+ A*VN('a', j)+ L*VN('l', j)+ P*VN('p', j) =g= k(j);
menores (j)  $(ord(j)> 2)      ..  C*VN('c', j)+ A*VN('a', j)+ L*VN('l', j)+ P*VN('p', j) =l= k(j);

Model model1 /all/ ;
option lp=CPLEX;
Solve model1 using lp min z;

Display C.l;
Display A.l;
Display L.l;
Display P.l;
Display z.l;
