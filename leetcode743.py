import sys
from _collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        N=N+1
        dist=[sys.maxsize]*(N)
        parent=[-1]*N
        processed=[False]*(N)
        graph=[[sys.maxsize]*(N) for _ in range(N)]
        for u,v,w in times:
            graph[u][v]=w
        dist[K] = 0
        for i in range(1,N):
            u = self.minkey(dist, processed,N)
            if u==None:continue
            processed[u] = True

            for v in range(1,N):
                if graph[u][v]!=sys.maxsize and processed[v]!=True:
                    if dist[v] > graph[u][v] + dist[u]:
                        dist[v] = graph[u][v] + dist[u]
        res=max(dist[1:])
        return -1 if res==sys.maxsize else res


    def minkey(self,dist,processed,N):
        min=sys.maxsize
        min_key=None
        for i in range(1,N):
            if not processed[i] and dist[i]<min:
                min_key=i
                min=dist[min_key]
        return min_key

sol=Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2))