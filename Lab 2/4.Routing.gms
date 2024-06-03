Sets
  i   Vértices / n1*n7 /
  k   Coordenadas /x, y/
  alias(j, i);


Table c(i, k) Coordenadas
    x   y
n1  20  6
n2  22  1
n3  9   2
n4  3   25
n5  21  10
n6  29  2
n7  14  12
;

Parameter d(i, j) Distancias;
Parameter vo Vértice inicial /4/;
Parameter vf Vértice final /6/;

loop((i, j),
    d(i, j)= sqrt( sqr(c(j, 'x')- c(i,'x')) + sqr(c(j,'y')-c(i,'y')));
    if (d(i,j)>20, d(i, j)=999;);
    if(sameas(i,j), d(i,j)=999;);
);

Variables
  x(i,j)      Indicates if the link i-j is selected or not.
  z           Objective function  ;

Binary Variable x;

Equations
objectiveFunction        objective function
sourceNode(i)            source node
destinationNode(j)       destination node
intermediateNode         intermediate node;

objectiveFunction                                  ..  z =e= sum((i,j), d(i,j) * x(i,j));

sourceNode(i)$(ord(i) = vo)                         ..  sum((j), x(i,j)) =e= 1;

destinationNode(j)$(ord(j) = vf)                    ..  sum((i), x(i,j)) =e= 1;

intermediateNode(i)$(ord(i) <> vo and ord(i) <> vf)  ..  sum((j), x(i,j)) - sum((j), x(j,i)) =e= 0;

Model model1 /all/ ;
option mip=cplex
Solve model1 using mip minimizing z;

Display 'Distancias: ', d;
Display 'Nodos seleccionados: ', x.l;
Display 'Distancia Total: ', z.l;