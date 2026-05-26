class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Approach 1: Recursion

        # def dfs(i, j):
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if i >= m or j >= n:
        #         return 0
        #     return dfs(i, j+1) + dfs(i+1, j)

        # return dfs(0, 0)


        # Approach 2: Dynamic Programming (Top - Down)

        # dp = [[-1] * n for _ in range(m)]
        
        # def dfs(i, j):
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if i >= m or j >= n:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
        #     return dp[i][j]

        # return dfs(0, 0)


        # Approach 3: Dynamic Programming (Bottom - Up)

        # dp = [[0] * (n+1) for _ in range(m+1)]
        # dp[m-1][n-1] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         dp[i][j] += dp[i+1][j] + dp[i][j+1]

        # return dp[0][0]


        # Approach 4: Dynamic Programming (Space Optimized)

        # dp = [1] * n

        # for i in range(m-1):
        #     temp = [1] * n
        #     for j in range(n-2, -1, -1):
        #         temp[j] = temp[j+1] + dp[j]
        #     dp = temp

        # return dp[0]


        # Approach 5: Dynamic Programming (Optimal)

        # dp = [0] * (n+1)
        # dp[n-1] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         dp[j] += dp[j+1]

        # return dp[0]


        # Approach 6: Math

        if m == 1 or n == 1: return 1

        if m > n:
            m, n = n, m

        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1
        
        return res