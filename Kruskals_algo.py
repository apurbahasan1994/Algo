"""steps >>>>
step1: sort all the edges in increasing order (lowest cost edges at first)
step2: pick the smallest edge:
    i) check the new edge forms circle or not
    ii)if cycle is not formed include that edge otherwise discard it.

Repeat the step 2 for (V-1) (total number of edge-1)times >>>>

"""
edge_list=[[0,1],[0,2],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[3,5],[4,5]] # edges in graph
num_of_nodes=6 # total num of nodes or vertex
cost_array=[1,2,3,1,3,2,1,2,4,3] #cost of each edge

def find(v,parent):
    """this function used to find the absolute parent of a node"""
    q = []
    while parent[v] != -1:
        q.append(v)
        v = parent[v]
    for i in range(len(q)):
        parent[q[i]] = v
    return v

def union(fromp,top,parent,rank):
    """this function is used to join two nodes"""
    if rank[fromp] < rank[top]:
        parent[fromp] = top
        rank[top] += 1
    if rank[fromp] > rank[top]:
        parent[top] = fromp
        rank[fromp] += 1

    else:
        parent[fromp] = top
        rank[parent[fromp]] += 1

def krushkals_algo(edge_list,cost_array,num_of_nodes):
    """this is the main function"""
    """step1: sort the edge list"""
    edge_list = [x for x, y in sorted(zip(edge_list,cost_array), key=lambda x: x[1])]
    cost_array.sort()
    parent=[-1]*num_of_nodes
    rank=[0]*num_of_nodes
    result=[]
    print(edge_list)
    """loop every edge and select. If it doest not create cycle select and joint it"""
    for i in range(len(edge_list)):
        fromp=find(edge_list[i][0],parent)
        top=find(edge_list[i][1],parent)
        print(edge_list[i][0],fromp,parent[edge_list[i][0]])
        print(edge_list[i][1],top,parent[edge_list[i][1]])
        if fromp==top:
            continue
        else:
            union(fromp, top, parent, rank)
            result.append([edge_list[i][0], edge_list[i][1]])
    return result

print(krushkals_algo(edge_list,cost_array,num_of_nodes))


