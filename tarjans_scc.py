
graph={
    0:[1],
    1:[2,3],
    3:[4],
    4:[0,5,6],
    5:[2,6],
    6:[5]
}
num_of_vertices=7


def dfs(disc, low, instack, stack, time, visited, root):
    visited[root]=True
    time+=1
    disc[root]=low[root]=time
    instack[root]=True
    stack.append(root)
    le = len(stack)
    if root not in graph.keys():
        if disc[root] == low[root]:
            stack.pop(root)
            print('scc is', end=' ')
            print(root)
            print('*' * 10)
            le-=1
            return
    for neighbors in graph[root]:
        if not visited[neighbors]:
            dfs(disc,low,instack,stack,time,visited,neighbors)
            low[root]=min(low[root],low[neighbors])
        else:
            if instack[neighbors]:
                low[root]=min(low[root],disc[neighbors])
            else:
                continue

    if disc[root] == low[root]:
        # stack.pop()
        # print(root)
        print('scc is', end=' ')
        while True:
            u=stack.pop()
            print(u)
            instack[u]=False
            if u==root:
                break


def Tarjans_SCC():
    disc=[-1]*num_of_vertices # discovery time at first all are -1
    low=[-1]*num_of_vertices # low time at first all are -1
    instack=[False]*num_of_vertices # at first there is no nodes in stack
    stack=[] # emplty stack
    visited=[False]*num_of_vertices
    time=0 # time is 0
    root=0

    """first  dfs travarsal """
    dfs(disc,low,instack,stack,time,visited,root)

    for i in range(max(disc)):
        ans = []
        for j in range(1,max(disc)):
            if low[i]==low[j] and i!=j:
                ans.append([i,j])
            else:
                break
        print(ans)


Tarjans_SCC()