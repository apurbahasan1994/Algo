from _collections import  defaultdict
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        cont=[0]*n
        graph=[[0]*n for _ in range(n)]
        for items in roads:
            cont[items[0]]+=1
            cont[items[1]]+=1
            graph[items[0]][items[1]]=1
            graph[items[1]][items[0]]=1
        rank=0
        for i in range(n):
            for j in range(n):
                if i==j:continue
                rank=max(rank,(cont[i]+cont[j]-graph[i][j]))
        return rank




sol=Solution()
sol.maximalNetworkRank(n=5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])

