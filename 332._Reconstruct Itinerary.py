from _collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)

        for key, values in graph.items():
            values.sort()
        source = 'JFK'
        ans = []
        stack = [source]

        while stack:
            while graph[stack[-1]]:
                neighbor = graph[stack[-1]].pop(0)
                stack.append(neighbor)
            ans.append(stack.pop())
        ans.reverse()
        return ans

        self.dfs( source, graph, ans,stack)
        print(ans)


sol = Solution()
print(sol.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
