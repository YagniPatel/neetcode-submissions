class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # Approach 1: Recursion

        # def dfs(i, j):
        #     if j == len(word2):
        #         return len(word1) - i
        #     if i == len(word1):
        #         return len(word2) - j

        #     if word1[i] == word2[j]:
        #         return dfs(i+1, j+1)
        #     res = min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
        #     return res + 1

        # return dfs(0, 0)


        # Appraoch 2: Dynamic Programming (Top - Down)

        # dp = {}

        # def dfs(i, j):
        #     if j == len(word2):
        #         return len(word1) - i
        #     if i == len(word1):
        #         return len(word2) - j
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     if word1[i] == word2[j]:
        #         dp[(i, j)] = dfs(i+1, j+1)
        #     else:
        #         res = min(dfs(i+1, j), dfs(i+1, j+1), dfs(i, j+1))
        #         dp[(i, j)] = res + 1
        #     return dp[(i, j)]

        # return dfs(0, 0)


        # Approach 3: Dynamic Programming (Bottom - Up)

        # m, n = len(word1), len(word2)
        # dp = [[0] * (n+1) for _ in range(m+1)]

        # for i in range(m+1):
        #     dp[i][n] = m - i
        # for j in range(n+1):
        #     dp[m][j] = n - j

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if word1[i] == word2[j]:
        #             dp[i][j] = dp[i+1][j+1]
        #         else:
        #             dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        # return dp[0][0]


        # Approach 4: Dynamic Programming (Space Optimized)

        # m, n = len(word1), len(word2)
        # if m < n:
        #     word1, word2 = word2, word1
        #     m, n = n, m

        # dp = [0] * (n+1)
        # tmp = [0] * (n+1)

        # for i in range(n+1):
        #     dp[i] = n - i

        # for i in range(m-1, -1, -1):
        #     tmp[n] = m - i
        #     for j in range(n-1, -1, -1):
        #         if word1[i] == word2[j]:
        #             tmp[j] = dp[j+1]
        #         else:
        #             tmp[j] = 1 + min(dp[j], dp[j+1], tmp[j+1])
        #     dp = tmp[:]

        # return dp[0]


        # Appraoch 5: Dynamic Programming (Optimal)

        m, n = len(word1), len(word2)
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m

        dp = [0] * (n+1)
        for i in range(n+1):
            dp[i] = n - i

        for i in range(m-1, -1, -1):
            pre = dp[n]
            dp[n] = m - i 
            for j in range(n-1, -1, -1):
                tmp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = pre
                else:
                    dp[j] = 1 + min(dp[j], dp[j+1], pre)
                pre = tmp

        return dp[0]