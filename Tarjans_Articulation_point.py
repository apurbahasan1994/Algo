# graph={
#     0:[1,2,3],
#     1:[0,2],
#     2:[0],
#     3:[0,4,5],
#     4:[3],
#     5:[3]
# }
graph={0: [1, 2], 1: [0, 2, 3], 2: [1, 0], 3: [1]}
num_of_vertices=6


# def dfs(disc, low, parent, child, visited, AP, time,current):
# def dfs(disc, low, parent,child visited, AP, time,current):
def dfs(disc, low, parent, child, visited, AP, time,current):

    visited[current]=True
    disc[current]=low[current]=time
    time += 1
    # child=0
    for neighbors in graph[current]:
        if not visited[neighbors]:
            child[current] += 1
            # child+=1
            parent[neighbors] = current
            # print(current,neighbors)
            # print(time)
            dfs(disc,low,parent,child,visited,AP,time,neighbors)
            # dfs(disc, low, parent, visited, AP, time,neighbors)
            low[current]=min(low[current],low[neighbors])

        if parent[current] == -1 and child[current] > 1:
            AP[current] = True
        if parent[current]!=-1 and disc[current]<low[neighbors]:
            AP[current]=True

        else:
            if parent[current]!=neighbors:
                low[current]=min(low[current],disc[neighbors])





def tarjans_ap():
    disc=[-1]*num_of_vertices
    low=[-1]*num_of_vertices
    parent=[-1]*num_of_vertices
    visited=[False]*num_of_vertices
    child =[0]*num_of_vertices
    AP=[False]*num_of_vertices
    time=0
    root=0
    dfs(disc,low,parent,child,visited,AP,time,root)
    # dfs(disc, low, parent, visited, AP, time, root)
    # print(AP)
    # print(parent)
    # print(child)
    # print(low)
    print(disc)
    print(low)

tarjans_ap()