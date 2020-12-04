import math
obj=[1,2,3,4,5,6,7]
profit=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
n=7
m=15
processed=[False]*(len(obj)+1)
def knapsack(profit,weight,m):
    ration=[]
    fractions=[0]*len(obj)
    for i in range(len(obj)):
        ration.append(profit[i]/weight[i])

    def maxkey():
        key = 0
        index=None
        for i in range(len(obj)):
            if processed[i]==False and ration[i] >=key:
                index = i
                key = ration[i]
        return index

    p=0

    for i in range(len(obj)):
        u = maxkey()
        if u==None:continue
        processed[u]=True
        if not weight[u] > m:
            fractions[u] = 1
            m-=weight[u]
            p+=profit[u]
        else:
            fractions[u]=m/weight[u]
            p+=fractions[u]*profit[u]
            break

    return p

print(knapsack(profit,weight,m))
