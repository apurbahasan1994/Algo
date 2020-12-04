from collections import defaultdict
import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        graph=defaultdict(list)
        heap=[]
        for (u,v),w in zip(edges,succProb):
            graph[u].append((v,w))
            graph[v].append((u,w))
        dist=[0.0]*n
        heapq.heappush(heap,(-1.0,start))
        dist[start]=1.0
        while heap:
            p,node=heapq.heappop(heap)
            p=-p
            if node==end:
                return p
            if dist[node]>p:
                continue

            for v,w in graph[node]:
                if dist[v]<p*w:
                    dist[v]=p*w
                    heapq.heappush(heap,(-(p*w),v))
        return 0




sol=Solution()
print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))