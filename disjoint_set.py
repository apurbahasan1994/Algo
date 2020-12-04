class Solution(object):
    def  findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # print(len(edges))
        parent = [-1] *(len(edges)+1)
        ans=self.cycle(edges, parent)
        return ans
    def cycle(self,edges,parent):
        ans=[]
        for p in edges:
            fromp=self.find(p[0],parent)
            top=self.find(p[1],parent)
            if fromp==top:
                True
            else:
                self.union(p[0],p[1],parent)
        return ans.pop()


    def find(self,v,parent):
        while True:
            if parent[v]==-1:
                return v
            else:
                v=parent[v]

    def union(self,fromp,top,parent):
        fromp=self.find(fromp,parent)
        top=self.find(top,parent)
        parent[top]=fromp



sol=Solution()
print(sol.findRedundantDirectedConnection([[5,2],[5,1],[3,1],[3,4],[3,5]]
))