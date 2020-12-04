class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """

        q=[]
        source=0
        childrenNodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in childrenNodes:
                source = i
        q=[source]
        visited=set()
        while q:
            u=q.pop(0)
            if u in visited:
                return False
            visited.add(u)
            if leftChild[u]!=-1:
                q.append(leftChild[u])
            if rightChild[u]!=-1:
                q.append(rightChild[u])
        return len(visited)==n

so=Solution()
print(so.validateBinaryTreeNodes( n = 2, leftChild = [1,0], rightChild = [-1,-1]))
