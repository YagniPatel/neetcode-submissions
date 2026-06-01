class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # Approach 1: Recursion
        
        # if len(t) > len(s): return 0

        # def dfs(i, j):
        #     if j >= len(t):
        #         return 1
        #     if i >= len(s):
        #         return 0

        #     res = dfs(i+1, j)
        #     if s[i] == t[j]:
        #         res += dfs(i+1, j+1)
        #     return res

        # return dfs(0, 0)


        # Approach 2: Dynamic Programming (Top - Down)

        # if len(t) > len(s): return 0
        # dp = {}

        # def dfs(i, j):
        #     if j >= len(t):
        #         return 1
        #     if i >= len(s):
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     res = dfs(i+1, j)
        #     if s[i] == t[j]:
        #         res += dfs(i+1, j+1)
        #     dp[(i, j)] = res
        #     return res

        # return dfs(0, 0)


        # Approach 3: Dynamic Programming (Bottom-Up)

        # m, n = len(s), len(t)
        # dp = [[0] * (n+1) for _ in range(m+1)]

        # for i in range(m+1):
        #     dp[i][n] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         dp[i][j] = dp[i+1][j]
        #         if s[i] == t[j]:
        #             dp[i][j] += dp[i+1][j+1]

        # return dp[0][0]


        # Approach 4: Dynamic Programming (Space Optimized)

        # m, n = len(s), len(t)
        # dp = [0] * (n+1)
        # tmp = [0] * (n+1)

        # dp[n] = tmp[n] = 1
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         tmp[j] = dp[j]
        #         if s[i] == t[j]:
        #             tmp[j] += dp[j+1]
        #     dp = tmp[:]

        # return dp[0]


        # Approach 5: Dynamic Programming (Optimal)

        m, n = len(s), len(t)
        dp = [0] * (n+1)
        dp[n] = 1

        for i in range(m-1, -1, -1):
            tmp = 1
            for j in range(n-1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += tmp
                tmp = dp[j]
                dp[j] = res
        
        return dp[0]