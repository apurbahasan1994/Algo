from collections import defaultdict
class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        ans=[0]*n
        graph=defaultdict(list)
        for edges in paths:
            graph[edges[0]].append(edges[1])
            graph[edges[1]].append(edges[0])
        print(graph)

        for i in range(1,n+1):
            print(i)
            colors=set([1,2,3,4])
            for neighbors in graph[i]:
                print(f'neig {neighbors}')
                if ans[neighbors-1] in colors:
                    colors.remove(ans[neighbors-1])
                print(f'colors{colors}')
            ans[i-1]=colors.pop()
            print(ans)
            print('**')

        return ans


sol=Solution()
print(sol.gardenNoAdj( n = 5, paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]))

