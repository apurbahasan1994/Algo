from _collections import defaultdict
class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        indegree = [0] *(n+1)
        graph=defaultdict(list)
        for edge in dependencies:
            graph[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        print(indegree)
        print(graph)
        q=[]
        for i in range(1,n+1):
            if indegree[i]==0:
                q.append(i)
        count=0
        ans=0
        while q:
            u=q.pop()



sol=Solution()
sol.minNumberOfSemesters( n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2)
