import sys
# graph=[[0,1,4,0,0,0],[1,0,4,2,7,0],[4,4,0,3,5,0],[0,2,3,0,4,6],[0,7,2,4,0,7],[0,0,0,6,7,0]]
# V=6
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
r = len(edges)
c = len(edges[0])

graph = [[sys.maxsize] * r for _ in range(r)]
for s, d, w in edges:
    graph[s][d] = w
    graph[d][s] = w
def minKey(dist,processed):
    mini=sys.maxsize
    min_index=None
    for i in range(n):
        if processed[i]==False and dist[i]<mini:
            min_index=i
            mini=dist[min_index]
    return min_index
def dikjstra(graph,n):
    parent=[-1]*n
    dist=[sys.maxsize]*n
    processed=[False]*6
    dist[0]=0
    for _ in range(1,n-1):
        u=minKey(dist,processed)
        # if u==None:continue
        processed[u]=True

        for v in range(n):
            if graph[u][v]!=sys.maxsize and dist[u]!=sys.maxsize:
                if dist[v]>graph[u][v]+dist[u]:
                    dist[v]=graph[u][v]+dist[u]
                    parent[v]=u
    for i in range(1,n):
        print(parent[i],i,graph[i][parent[i]])
    return dist
print(dikjstra(graph,n))







