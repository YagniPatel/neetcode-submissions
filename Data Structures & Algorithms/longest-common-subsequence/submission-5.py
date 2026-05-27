class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Approach 1: Recursion

        # def dfs(i, j):
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + dfs(i+1, j+1)
        #     return max(dfs(i+1, j), dfs(i, j+1))

        # return dfs(0, 0)


        # Approach 2: Dynammic Programming (Top-Down)

        # dp = {}

        # def dfs(i, j):
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     if text1[i] == text2[j]:
        #         dp[(i, j)] = 1 + dfs(i+1, j+1)
        #     else:
        #         dp[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
        #     return dp[(i, j)]

        # return dfs(0, 0)


        # Approach 3: Dynamic Programming (Bottom - Up)

        # m, n = len(text1), len(text2)
        # dp = [[0] * (n+1) for _ in range(m+1)]

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # return dp[0][0]


        # Approach 4: Dynamic Programming (Space Optimized)

        # if len(text1) < len(text2):
        #     text1, text2 = text2, text1

        # pre = [0] * (len(text2) + 1)
        # cur = [0] * (len(text2) + 1)

        # for i in range(len(text1)-1, -1, -1):
        #     for j in range(len(text2)-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             cur[j] = 1 + pre[j+1]
        #         else:
        #             cur[j] = max(cur[j+1], pre[j])
        #     pre, cur = cur, pre

        # return pre[0]


        # Approach 5: Dynamic Programming (Optimal)

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1)-1, -1, -1):
            pre = 0
            for j in range(len(text2)-1, -1, -1):
                tmp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + pre
                else:
                    dp[j] = max(dp[j+1], dp[j])
                pre = tmp
            
        return dp[0]