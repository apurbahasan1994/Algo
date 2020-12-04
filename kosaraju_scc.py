"""algo>>>>>>>>>
   step1:performs dfs on graph and push node to stack before returning
   step2:find the transpose graph by reversing edges
   step3:pop nodes one by one form stack and again do dfs on modified graph

"""

from collections import defaultdict

graph = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5], [4, 7], [5, 6], [6, 7], [6, 4]]
num_of_vertex = 8


def dfs(visited, graph_dict, i, stack):
    visited[i] = True  # mark the current node visited
    """ check if the current node present in the key of the dict 
        if that not in dict.keys() that means there is no nodes to travarse.
        push the node into stack and return.
    """
    if i not in graph_dict.keys():
        stack.append(i)
        return
    """if there is neighboring vertex present in current node and its not visited
       run dfs on it.
    """
    for neighbors in graph_dict[i]:
        if not visited[neighbors]:
            dfs(visited, graph_dict, neighbors, stack)
    stack.append(i)  # while returning push the current node to stack


def transpose():
    """use for reversing the edges"""
    d = defaultdict(list)
    graphnew = sorted(graph, key=lambda x: x[1])
    for i in range(len(graphnew)):
        d[graphnew[i][1]].append(graphnew[i][0])
    return d


def dfs2(visited, current_vertex, reversed_graph):
    """used for dfs travarsal on the transposed graph"""
    print(current_vertex)
    visited[current_vertex] = True
    for neighbors in reversed_graph[current_vertex]:
        if not visited[neighbors]:
            dfs2(visited, neighbors, reversed_graph)


def kosaraju():
    """main algorithm"""
    """step:1"""

    visited = [False] * num_of_vertex  # tracks all the visited nodes
    stack = []  # stack for adding the nodes from dfs travarsal
    graph_dict = defaultdict(list)  # create defaultdict to create adjecency list

    for i in range(len(graph)):  # loop creates adjecency list
        graph_dict[graph[i][0]].append(graph[i][1])

    """form o->n pick a node if its visited than do nothing
       if not visited run dfs on the node to visit its adjecent nodes
    """
    for i in range(num_of_vertex):
        if not visited[i]:
            dfs(visited, graph_dict, i, stack)

    """step:2"""

    reversed_graph = transpose()  # reverse the edges
    visited = [False] * num_of_vertex  # mark all nodes to unvisited

    """step:3"""

    """ untill the stack in empty:
                    pop a node from the top of stack 
                    check it already visited or not
                    if not visited run dfs on the node.

    """
    while stack:
        current_vertex = stack.pop()
        if not visited[current_vertex]:
            dfs2(visited, current_vertex, reversed_graph)
            print('*' * 10)


kosaraju()

