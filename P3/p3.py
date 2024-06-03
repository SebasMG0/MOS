g=[
    [(1, 2), (2, 4), (3, 6)],
    [(0, 2), (3, 1), (4, 3)],
    [(0, 4), (3, 3), (4, 1)],
    [(0, 6), (1, 1), (2, 3)],
    [(1, 3), (2, 1)]
]       


a= [[0]*len(g) for _ in range(len(g))]


for i in range(len(g)):
    for j in g[i]:
        a[i][j[0]]= j[1]

for i in a:
    print(i)