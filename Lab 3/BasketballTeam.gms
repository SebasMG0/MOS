Sets
    player /1*7/
    role  /ataque, centro, defensa/
    property /control, disparo, rebotes, defensa/;

Table roles(player, role)
       ataque  centro  defensa
1      1       0       0
2      0       1       0
3      1       0       1
4      0       1       1
5      1       0       1
6      0       1       1
7      1       0       1
;

Table properties(player, property)
       control  disparo  rebotes  defensa
1      3              3        1        3
2      2              1        3        2
3      2              3        2        2
4      1              3        3        1
5      3              3        3        3
6      3              1        2        3
7      3              2        2        1
;

Parameters
    numPlayers /5/,
    propertiesRestrictions(property) /control 2, disparo 2, rebotes 2, defensa 0/,
    rolesRestriction(role) /ataque 2, centro 1, defensa 4/
;


Binary Variables p(player);
variable z;
    
Equations
    objectiveFunction,
    numPlayersCondition 5 jugadores,
    playerUnicity Está el 2 o el 3,
    rolCondition(role) Al menos x en k posición,
    propertyCondition(property) Promedio del equipo;
    

objectiveFunction                .. z=e= sum(player, p(player)*properties(player, 'defensa') );
numPlayersCondition              .. sum(player, p(player)) =e= numPlayers;
playerUnicity                    .. p('2')+p('3')=e=1;
rolCondition(role)               .. sum(player, p(player)*roles(player, role))=g=rolesRestriction(role);
propertyCondition(property)      .. sum(player, p(player)*properties(player, property))/numPlayers=g=propertiesRestrictions(property);



Model model1 /all/ ;
option mip=cplex;
Solve model1 using mip maximizing z;

display 'Valor máximo en defensa: ' z.l;
display 'Jugadores escogidos: ', p.l;
