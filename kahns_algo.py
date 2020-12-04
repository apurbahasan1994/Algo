class Solution(object):
    def findOrder(self,numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * numCourses
        graph = {}
        res=[]
        for i in range(len(prerequisites)):
            indegree[prerequisites[i][0]] += 1

        for i in range(len(prerequisites)):
            if prerequisites[i][1] in graph.keys():
                graph[prerequisites[i][1]].append(prerequisites[i][0])
            else:
                graph[prerequisites[i][1]] = [prerequisites[i][0]]

        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in graph.keys():
                graph[prerequisites[i][0]]=[]
        print(graph)



        q = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        count=0
        while q:
            u = q.pop()
            res.append(u)
            try:
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
                count+=1

            except KeyError:
                pass

        if(count!=numCourses):
            return []
        return res


sol=Solution()
print(sol.findOrder(2,[[1,0]]))