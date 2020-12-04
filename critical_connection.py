from collections import defaultdict
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(connections)
        graph=defaultdict(list)
        for i in range(m):
            graph[connections[i][0]].append(connections[i][1])
            graph[connections[i][1]].append(connections[i][0])
        print(graph)

        lowtime=[0]*n
        discovertime=[0]*n
        visited=[False]*n
        root=list(graph.keys())[0]
        time=0
        result=[]
        self.dfs(visited,root, -1, lowtime, discovertime, time, graph, result)
        print(discovertime)
        print(lowtime)
        return result

    def dfs(self,visited,current,parent,lowtime,discovertime,time,graph,result):
        visited[current]=True
        lowtime[current]=discovertime[current]=time
        time += 1
        for neighbors in graph[current]:
            if neighbors == parent:
                continue
            if not visited[neighbors]:
                self.dfs(visited,neighbors,current,lowtime,discovertime,time,graph,result)
                lowtime[current]=min(lowtime[current],lowtime[neighbors])
                if discovertime[current]<lowtime[neighbors]:
                    result.append([current,neighbors])

            else:
                lowtime[current]=min(lowtime[current],discovertime[neighbors])



sol=Solution()
print(sol.criticalConnections(4,[[0, 1], [1, 2], [2, 0], [1, 3]]))