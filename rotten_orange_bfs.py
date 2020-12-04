class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        q = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1

        minute = 0
        while q:
            i, j, minute = q.pop(0)
            print(minute)
            if grid[i][j] == 2:
                for r, c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c, minute + 1))

        if fresh > 0:
            return -1
        else:
            return minute
sol=Solution()
input=[[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(input))