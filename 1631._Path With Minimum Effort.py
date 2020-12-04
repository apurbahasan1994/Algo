import sys
import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m=len(heights)
        n=len(heights[0])
        """ absolute difference of two elements of an array A is defined as |A[i] – A[j]| + |i – j|
         where |A| denotes the absolute value of A."""

        min_efforts=[[sys.maxsize]*n for _ in range(m)]
        min_efforts[0][0]=0
        pq=[(0,0,0)]
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        visited_set=set()
        while pq:
            min_e,i,j=heapq.heappop(pq)
            visited_set.add((i,j))
            for d in directions:
                new_i=i+d[0]
                new_j=j+d[1]
                if new_i >= 0 and new_i < m and new_j >= 0\
                        and new_j < n and (new_i,new_j) not in visited_set:
                    new_min_e=max(abs(heights[i][j]-heights[new_i][new_j]),min_e)
                    if new_min_e < min_efforts[new_i][new_j]:
                        heapq.heappush(pq, (new_min_e, new_i, new_j))
                        min_efforts[new_i][new_j] = new_min_e

        return min_efforts[-1][-1]


