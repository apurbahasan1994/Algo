import sys
from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph=defaultdict(list)
        indegree=[0]*n
        for source, dest in edges:
            graph[source].append(dest)
            graph[dest].append(source)
            indegree[source]+=1
            indegree[dest]+=1
        parent=[i for i in indegree if indegree[i]>1]
        print(parent)


        def dfs(i):
            source=i
            stack=[(i,0)]
            visited=[False]*n
            temp=-1
            while stack:
                u,cont=stack.pop()
                visited[u]=True
                for neighbors in graph[u]:
                    if not visited[neighbors]:
                        stack.append((neighbors,cont+1))
                if cont>temp:
                    temp=cont
            return temp

        ans=[]
        for i in range(n):
            if indegree[i]>1:
                h=dfs(i)
                ans.append(h)
        return ans
        # result=[]
        # for i in range(len(ans)):
        #     if ans[i] == min(ans):
        #         result.append(i)
        # return ans

sol=Solution()
print(sol.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))