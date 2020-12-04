import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        seive=[1]*(n)
        seive[0]=seive[1]=0
        for i in range(2,(int)(math.sqrt(n)) + 1):
            if seive[i]==1:
                for j in range(i * i,n,i):
                    seive[j]=0
        return sum(seive)
sol=Solution()
print(sol.countPrimes(15))

