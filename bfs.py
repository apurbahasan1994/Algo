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
def bfs(graph,root):
    queue.append(root)
    visited.append(root)
    while(len(queue)):
        v=queue.pop(0)
        print(v)
        for values in graph[v]:
            if values not in visited:
                queue.append(values)
                visited.append(values)
bfs(graph,0)