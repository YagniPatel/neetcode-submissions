class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # Approach 1: Recursion

        # def dfs(k, i, j):
        #     if k >= len(s3):
        #         return i == len(s1) and j == len(s2)

        #     if i < len(s1) and s3[k] == s1[i]:
        #         if dfs(k+1, i+1, j):
        #             return True
        #     if j < len(s2) and s3[k] == s2[j]:
        #         if dfs(k+1, i, j+1):
        #             return True

        #     return False

        # return dfs(0, 0, 0)


        # Approach 2: Dynamic Programming (Top - Down)

        # dp = {}

        # def dfs(k, i, j):
        #     if k >= len(s3):
        #         return i == len(s1) and j == len(s2)
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     res = False
        #     if i < len(s1) and s3[k] == s1[i]:
        #         res = dfs(k+1, i+1, j)
        #     if j < len(s2) and s3[k] == s2[j]:
        #         res = dfs(k+1, i, j+1)

        #     dp[(i, j)] = res
        #     return res

        # return dfs(0, 0, 0)


        # Approach 3: Dynamic Programming (Bottom - Up)

        # if len(s1) + len(s2) != len(s3):
        #     return False

        # dp = [[False] * (len(s2)+1) for _ in range(len(s1) + 1)]
        # dp[len(s1)][len(s2)] = True

        # for i in range(len(s1), -1, -1):
        #     for j in range(len(s2), -1, -1):
        #         if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
        #             dp[i][j] = True
        #         if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
        #             dp[i][j] = True

        # return dp[0][0]


        # Approach 4: Dynamic Programming (Space Optimized)

        # m = len(s1)
        # n = len(s2)
        # if m + n != len(s3):
        #     return False

        # if m > n:
        #     s1, s2 = s2, s1
        #     m, n = n, m

        # dp = [False] * (m+1)
        # dp[m] = True

        # for i in range(n, -1, -1):
        #     tmp = [False] * (m+1)
        #     if i == n:
        #         tmp[m] = True
        #     for j in range(m, -1, -1):
        #         if i < n and s2[i] == s3[i+j] and dp[j]:
        #             tmp[j] = True
        #         if j < m and s1[j] == s3[i+j] and tmp[j+1]:
        #             tmp[j] = True
        #     dp = tmp

        # return dp[0]


        # Approach 5: Dynamic Programming (Optimal)

        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False

        if m > n:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False] * (m+1)
        dp[m] = True

        for i in range(n, -1, -1):
            tmp = True if i == n else False
            for j in range(m, -1, -1):
                res = False if j < m else tmp
                if i < n and s2[i] == s3[i+j] and dp[j]:
                    res = True
                if j < m and s1[j] == s3[i+j] and tmp:
                    res = True
                dp[j] = res
                tmp = dp[j]

        return dp[0]