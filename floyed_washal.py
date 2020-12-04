from copy import deepcopy
INF=999
graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]
V=4

def floyed_washal():
    dist=deepcopy(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j]=min(dist[i][j],(dist[i][k]+dist[k][j]))

    for i in range(V):
        for j in range(V):
            if i==j and dist[i][j]<0:
                print('cycle')
                break
    print(dist)

floyed_washal()