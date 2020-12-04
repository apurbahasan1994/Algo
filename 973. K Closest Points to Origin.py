import math


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        ans=[]
        for point in points:
            dist=math.sqrt(pow(0-point[0],2)+pow(0-point[1],2))
            ans.append((dist,point))
        ans=sorted(ans,key=lambda x:x[0])
        result=[]
        for res in ans:
            result.append(res[1])
        return result[0:K]
sol=Solution()
print(sol.kClosest( points = [[3,3],[5,-1],[-2,4]], K = 2))
