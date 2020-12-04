graph={
    0:[3,1],
    1:[0,3,5,6,2],
    3:[0,1,4,2],
    2:[1,5,4,3],
    5:[1,2],
    4:[2,3,6],
    6:[1,4]
}
stack=[]
visited=[]
def dfs(graph,root):
    stack.append(root)
    visited.append(root)
    while(len(stack)):
        v=stack.pop()
        print(v,end=' ')
        for neighbors in graph[v]:
            if neighbors not in visited:
                stack.append(neighbors)
                visited.append(neighbors)

dfs(graph,0)