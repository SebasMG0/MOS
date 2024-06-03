Sets
    i Objetos (filas) /a, b, c, d, e/
    j  Valor y peso de los objetos (columnas) /Valor, Peso/;
    
Table knap(i, j)
    Valor   Peso
a   12       9
b   5        2
c   9        2
d   6        1
e   4        3 ;
  
Variables
  z     Función objetivo;

Binary Variable X(i);

Scalar p Peso alcanzado por los objetos en la maleta;

Parameters W Peso máximo /10/;

Equations
    objectiveFunction
    restriccionPeso;

objectiveFunction   ..  z =e= sum(i, X(i)*knap(i, 'valor'));

restriccionPeso     ..  sum(i, X(i)*knap(i, 'peso')) =l= W;


Model knapsack /all/;
Solve knapsack using MIP maximizing z;

p= sum(i, X.l(i)*knap(i, 'Peso'));

display 'Elementos escogidos:', X.l;
display 'Valor máximo alcanzado: ', z.l;
display 'Peso alcanzado: ', p;