class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        A_ptr=0
        B_ptr=0
        ans=[]
        while(A_ptr<len(A) and B_ptr<len(B)):
            if A[A_ptr][0]<=B[B_ptr][1] and A[A_ptr][1]>=B[B_ptr][0]:
                ans.append([max(A[A_ptr][0],B[B_ptr][0]),min(A[A_ptr][1],B[B_ptr][1])])
            if A[A_ptr][1] < B[B_ptr][1]:
                A_ptr += 1
            else:
                B_ptr += 1
        return ans

sol=Solution()
print(sol.intervalIntersection( A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))


