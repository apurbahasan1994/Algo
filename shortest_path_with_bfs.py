import sys
graph={
    0:[1,3],
    1:[0,2,3,5,6],
    3:[0,1,2,4],
    2:[1,3,4,5],
    5:[1,2],
    4:[2,3,6],
    6:[1,4]
}
queue=[]
visited=[]
dist=[sys.maxsize]*len(graph)
def bfs(graph,root):
    queue.append(root)
    visited.append(root)
    dist[root]=0
    while(len(queue)):
        u=queue.pop(0)
        for values in graph[u]:
            if values not in visited:
                queue.append(values)
                visited.append(values)
                dist[values]=dist[u]+1
    print(dist)
bfs(graph,0)