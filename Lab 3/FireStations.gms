Sets
    i /p1*p6/
    alias(j, i);

table tiempo(i,j)
    p1  p2  p3  p4  p5  p6
p1  0   10  20  30  30  20
p2  10  0   25  35  20  10
p3  20  25  0   15  30  20
p4  30  35  15  0   15  25
p5  30  20  30  15  0   14
p6  20  10  20  25  14  0;

Parameter y(i, j);

loop ((i, j),
    if (tiempo(i, j) <= 15, y(i, j)=1)
);

Binary Variables x(i);
variables z;

Equations
    objectiveFunction
    coberturaTotal (j);

objectiveFunction    ..  z =e= sum(i, x(i));
coberturaTotal (j)   ..  sum(i, x(i)*y(i, j)) =g= 1;

Model vertexCover /all/;
option mip=cplex;
Solve vertexCover using MIP minimizing z;

display '-> Pueblos en los que se van a construir estaciones: ', x.l;
