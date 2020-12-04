class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        print(n)

        def coin_change(amount, n):
            t = [[0] * (amount + 1) for _ in range(n + 1)]

            for i in range(n + 1):
                for j in range(amount + 1):
                    if i == 0:
                        t[i][j] = 0
                    if j == 0:
                        t[i][j] = 1
            for r in t:
                print(r)

            for i in range(1, n + 1):
                for j in range(1, amount + 1):
                    if coins[i - 1] <= j:
                        t[i][j] = t[i - 1][j] + t[i][j - coins[i - 1]]
                    else:
                        t[i][j] = t[i - 1][j]

            return (t[n][amount])
        ans=coin_change(amount,n)
        return ans
sol=Solution()
print(sol.change( amount = 5, coins = [1, 2, 5]))