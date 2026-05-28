class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Approach 1: Recursion

        # def dfs(i, buying):
        #     if i >= len(prices):
        #         return 0
        #     cooldown = dfs(i+1, buying)
        #     if buying:
        #         buy = dfs(i+1, not buying) - prices[i]
        #         return max(buy, cooldown)
        #     else:
        #         sell = prices[i] + dfs(i+2, not buying)
        #         return max(sell, cooldown)

        # return dfs(0, True)


        # Approach 2: Dynamic PRogramming (Top - Down)

        # dp = {}

        # def dfs(i, buying):
        #     if i >= len(prices):
        #         return 0
        #     if (i, buying) in dp:
        #         return dp[(i, buying)]
            
        #     cooldown = dfs(i+1, buying)
        #     if buying:
        #         buy = dfs(i+1, not buying) - prices[i]
        #         dp[(i, buying)] = max(buy, cooldown)
        #     else:
        #         sell = prices[i] + dfs(i+2, not buying)
        #         dp[(i, buying)] = max(sell, cooldown)

        #     return dp[(i, buying)]

        # return dfs(0, True)


        # Approach 3: Dynamic Programming (Bottom - Up)

        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n+1)]
        
        # for i in range(n-1, -1, -1):
        #     cooldown = dp[i+1][1] if i+1 < n else 0
        #     buy = dp[i+1][0] - prices[i] if i+1 < n else -prices[i]
        #     dp[i][1] = max(cooldown, buy)

        #     cooldown = dp[i+1][0] if i+1 < n else 0
        #     sell = dp[i+2][1] + prices[i] if i+2 < n else prices[i]
        #     dp[i][0] = max(cooldown, sell)

        # return dp[0][1]


        # Approach 4: Dynamic Programming (Space Optimized)

        n = len(prices)
        dp1 = [0] * 2
        dp2 = [0] * 2

        for i in range(n-1, -1, -1):
            tmp = [0] * 2

            cooldown = dp1[1]
            buy = dp1[0] - prices[i]
            tmp[1] = max(buy, cooldown)

            cooldown = dp1[0]
            sell = dp2[1] + prices[i]
            tmp[0] = max(sell, cooldown)

            dp1, dp2 = tmp, dp1

        return dp1[1]