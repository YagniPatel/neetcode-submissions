class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Approach 1: Recursion
        
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
            
        #     return cost[i] + min(dfs(i+1), dfs(i+2))

        # return min(dfs(0), dfs(1))


        # Approach 2: Dynamic Programming (Top-Down)

        # cache = [-1] * (len(cost))

        # def dfs(i):
        #     if i >= len(cost):
        #         return 0

        #     if cache[i] != -1:
        #         return cache[i]

        #     cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return cache[i]

        # return min(dfs(0), dfs(1))


        # Approach 3: Dynamic Programming (Bottom-Up)

        # n = len(cost)
        # dp = [0] * (n+1)

        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        # return dp[n]


        # Approach 4: Dynamic Programming (Space Optimized)

        n = len(cost)
        for i in range(n-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])