Sets
    i /c1*c8/
    j   /d1, d2/,
    tipo /blues, rock, n/,
    duracion /d/;
    

Parameter canciones(i, tipo)
    blues   rock    n
c1  1   0   0
c2  0   1   0
c3  1   0   0
c4  0   1   0
c5  1   0   0
c6  0   1   0
c7  0   0   1
c8  1   1   0;


 parameter duraciones(i, duracion)
    d
c1  4
c2  5
c3  3
c4  2
c5  4
c6  3
c7  5
c8  4;

parameters len /min 14, max 16/;
parameters requerimientos(tipo) /blues 2, rock 3, n 0/;


Variables z;
Binary Variable a(i), b(i);
Equations
    objectiveFunction,
    seleccion,
    longituda,
    longitudab,
    longitudb,
    longitudbb,
    reqa(tipo),
    reqb(tipo),
    r1,
    r2;
    
objectiveFunction              ..  z =e= sum(i, a(i) + b(i));
seleccion                      ..  sum(i, a(i) + b(i))=e= card(i);

longituda .. sum(i, a(i)*duraciones(i, 'd')) =g= len('min');
longitudab .. sum(i, a(i)*duraciones(i, 'd')) =l= len('max');
longitudb .. sum(i, b(i)*duraciones(i, 'd')) =g= len('min');
longitudbb .. sum(i, b(i)*duraciones(i, 'd'))  =l= len('max');

reqa (tipo)       .. sum(i, a(i)*canciones(i, tipo))=e= requerimientos(tipo);
reqb (tipo)       .. sum(i, b(i)*canciones(i, tipo))=e= requerimientos(tipo);

r1          ..  1-a('c3')=g= a('c5');
r2 .. a('c2') + a('c4') - a('c1') =l= 1;


Model model1 /all/ ;
option mip=cplex;
Solve model1 using mip maximizing z;

Display 'Cara A', a.l;
Display 'Cara B', b.l;

