class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        indegree=[0]*n
        for edge in edges:
            indegree[edge[1]]+=1
        ans=[]
        for i in range(n):
            if indegree[i]==0:
                ans.append(i)
        return ans

sol=Solution()
print(sol.findSmallestSetOfVertices( n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]))
