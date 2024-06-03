from sympy import symbols, Eq, solve

def find_vertices(restrictions):
    x1, x2 = symbols('x1 x2')
    vertices = []
    for i in range(len(restrictions)):
        for j in range(i+1, len(restrictions)):
            sol = solve((Eq(restrictions[i][0]*x1 + restrictions[i][1]*x2, restrictions[i][2]),
                         Eq(restrictions[j][0]*x1 + restrictions[j][1]*x2, restrictions[j][2])), (x1, x2))
            if sol and sol[x1] >= 0 and sol[x2] >= 0:
                vertices.append((sol[x1], sol[x2]))
    return vertices

def create_adjacency_list(vertices, restrictions):
    adjacency_list = [[] for _ in vertices]
    for i, vertex in enumerate(vertices):
        for restriction in restrictions:
            if restriction[0]*vertex[0] + restriction[1]*vertex[1] == restriction[2]:
                for j, other_vertex in enumerate(vertices):
                    if other_vertex != vertex and restriction[0]*other_vertex[0] + restriction[1]*other_vertex[1] <= restriction[2]:
                        adjacency_list[i].append(j)
    return adjacency_list

restrictions = [(2, 1, 100), (1, 1, 80), (1, 0, 40), (-1, 0, 0), (0, -1, 0)]
vertices = find_vertices(restrictions)
adjacency_list = create_adjacency_list(vertices, restrictions)

print(adjacency_list)
