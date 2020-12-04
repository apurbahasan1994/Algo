
def disJoint(n):
    parent=[-1]*(n)
    visited=[]
    rank=[0]*n
    edge_list=[[0,1],[2,3],[1,2],[0,4],[4,3]]
    print(cycle(edge_list,parent,rank))
    print(edge_list)
    print(parent[0:])
    print(rank[0:])


def union(fromp, top, parent,rank):
    if rank[fromp]<rank[top]:
        parent[fromp] = top
        rank[top]+=1
    if rank[fromp]>rank[top]:
        parent[top] = fromp
        rank[fromp]+=1

    else:
        parent[fromp]=top
        rank[parent[fromp]]+=1

def find(v,parent):
    q=[]
    while parent[v]!=-1:
        q.append(v)
        v = parent[v]
    for i in range(len(q)):
        parent[q[i]]=v
    return v

def cycle(edge_list,parent,rank):
    for p in edge_list:
        fromp=find(p[0],parent)
        top=find(p[1],parent)
        if fromp==top:
            return True
        else:
            union(fromp,top,parent,rank)
    return False

disJoint(5)