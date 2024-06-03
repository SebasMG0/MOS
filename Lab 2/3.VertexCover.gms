Sets
    i Nodo Origen (filas) /n1*n12/
    alias(j, i);

Table grafo(i, j)

    n1  n2  n3  n4  n5  n6  n7  n8  n9  n10 n11 n12
n1  1   1   1   0   1   0   0   0   0   0   0   0
n2  1   1   0   0   1   0   0   0   0   0   0   0
n3  1   0   1   1   1   1   1   1   0   0   0   0
n4  0   0   1   1   1   1   0   0   0   0   1   0
n5  1   1   1   1   1   0   0   0   0   1   1   0
n6  0   0   1   1   0   1   0   1   0   0   1   0
n7  0   0   1   0   0   0   1   1   0   0   0   1
n8  0   0   1   0   0   1   1   1   1   0   1   1
n9  0   0   0   0   0   0   0   1   1   1   1   1
n10 0   0   0   0   1   0   0   0   1   1   1   0
n11 0   0   0   1   1   1   0   1   1   1   1   0
n12 0   0   0   0   0   0   1   1   1   0   0   1
;

Binary Variables x(i);
variables z;

Equations
    objectiveFunction
    coberturaTotal (j);

objectiveFunction    ..  z =e= sum(i, x(i));
coberturaTotal (j)   ..  sum(i, x(i)*grafo(i, j)) =g= 1;

Model vertexCover /all/;
Solve vertexCover using MIP minimizing z;


display 'Vértices seleccionados:', X.l;