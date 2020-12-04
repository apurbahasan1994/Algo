import  sys
graph=[[0,4,6,0,0,0],[4,0,6,3,4,0],[6,6,0,1,0,0],[0,3,1,0,2,3],[0,4,0,2,0,7],[0,0,0,3,7,0]]
node=6
def mst(graph,node):
    parent = [-1] * 6
    mstSet = [False] * 6
    key = [sys.maxsize] * 6
    key[0]=0
    for _ in range(node-1):
        u=minKey(key,mstSet)
        mstSet[u]=True

        for v in range(node):
            if graph[u][v]!=0 and mstSet[v]==False and graph[u][v]<key[v]:
                parent[v]=u
                key[v]=graph[u][v]

    printMst(parent,node,graph)

def minKey(key,mstSet):
    # min_index=None
    mini=sys.maxsize
    for i in range(node):
        if mstSet[i]==False and key[i]<mini:
            min_index=i
            mini=key[min_index]
    return min_index

def printMst(parent,node,graph):
    for i in range(1,node):
        print(parent[i],i,graph[i][parent[i]])





mst(graph,node)