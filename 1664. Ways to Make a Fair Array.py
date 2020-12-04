class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        even_presum=[0]*(n+1)
        odd_presum=[0]*(n+1)
        for i,num in enumerate(nums):
            if i%2:
                odd_presum[i+1] = odd_presum[i] + num
                even_presum[i+1]=even_presum[i]
            else:
                even_presum[i+1] = even_presum[i] + num
                odd_presum[i+1]=odd_presum[i]
        ans=0
        for i in range(1,n+1):
            evensum1=even_presum[i-1]
            oddsum1=odd_presum[i-1]

            evensum2=odd_presum[-1]-odd_presum[i]
            oddsum2=even_presum[-1]-even_presum[i]
            if evensum1+evensum2==oddsum1+oddsum2:
                ans+=1

        return ans
sol=Solution()
print(sol.waysToMakeFair(nums = [2,1,6,4]))

