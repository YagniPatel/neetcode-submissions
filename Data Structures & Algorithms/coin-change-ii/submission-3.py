class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Approach 1: Recursion

        # def dfs(i, a):
        #     if a == 0:
        #         return 1
        #     if i >= len(coins):
        #         return 0

        #     res = 0
        #     if a >= coins[i]:
        #         res += dfs(i+1, a)
        #         res += dfs(i, a - coins[i])
        #     return res
        
        # coins.sort()
        # return dfs(0, amount)


        # Approach 2: Dynamic Programming (Top - Down)

        # n = len(coins)
        # dp = [[-1] * (amount+1) for _ in range(n+1)]

        # def dfs(i, a):
        #     if a == 0:
        #         return 1
        #     if i >= n:
        #         return 0
        #     if dp[i][a] != -1:
        #         return dp[i][a]

        #     res = 0
        #     if a >= coins[i]:
        #         res += dfs(i+1, a)
        #         res += dfs(i, a - coins[i])

        #     dp[i][a] = res
        #     return res

        # coins.sort()
        # return dfs(0, amount)


        # Approach 3: Dynamic Programming (Bottom - Up)

        # n = len(coins)
        # coins.sort()
        # dp = [[0] * (amount+1) for _ in range(n+1)]

        # for i in range(n+1):
        #     dp[i][0] = 1

        # for i in range(n-1, -1, -1):
        #     for a in range(amount+1):
        #         if a >= coins[i]:
        #             dp[i][a] = dp[i+1][a] + dp[i][a - coins[i]]
                
        # return dp[0][amount]


        # Approach 4: Dynamic Programming (Space Optimized)

        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1

        for i in range(n-1, -1, -1):
            for a in range(amount+1):
                if a >= coins[i]:
                    dp[a] += dp[a - coins[i]]

        return dp[amount]