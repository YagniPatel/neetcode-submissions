class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # Approach 1: Recursion
        
        # def dfs(i, open):
        #     if open < 0:
        #         return False
        #     if i >= len(s):
        #         return open == 0

        #     if s[i] == "(":
        #         return dfs(i + 1, open + 1)
        #     elif s[i] == ")":
        #         return dfs(i + 1, open - 1)
        #     else:
        #         return dfs(i + 1, open) or dfs(i + 1, open + 1) or dfs(i + 1, open - 1)

        # return dfs(0, 0)


        # Approach 2: Dynamic Programming

        # dp = {}

        # def dfs(i, open):
        #     if open < 0:
        #         return False
        #     if i >= len(s):
        #         return open == 0
        #     if (i, open) in dp:
        #         return dp[(i, open)]

        #     if s[i] == "(":
        #         dp[(i, open)] = dfs(i + 1, open + 1)
        #     elif s[i] == ")":
        #         dp[(i, open)] = dfs(i + 1, open - 1)
        #     else:
        #         dp[(i, open)] = dfs(i + 1, open) or dfs(i + 1, open + 1) or dfs(i + 1, open -1)

        #     return dp[(i, open)]

        # return dfs(0, 0)


        # Approach 3: Dynamic Programming (Bottom-Up)

        # n = len(s)
        # dp = [[False] * (n + 1) for _ in range(n + 1)]
        # dp[n][0] = True

        # for i in range(n - 1, -1, -1):
        #     for open in range(n):
        #         if s[i] == "(":
        #             dp[i][open] = dp[i + 1][open + 1]
        #         elif s[i] == ")":
        #             dp[i][open] = dp[i + 1][open - 1]
        #         else:
        #             dp[i][open] = dp[i + 1][open] or dp[i + 1][open + 1] or dp[i + 1][open - 1]
                
        # return dp[0][0]


        # Approach 4: Dynamic Programming (Space Optimized)

        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True

        # for i in range(n - 1, -1, -1):
        #     tmp = [False] * (n + 1)
        #     for open in range(n):
        #         if s[i] == "*":
        #             tmp[open] = dp[open + 1] or dp[open] or (dp[open - 1] and open > 0)
        #         elif s[i] == "(":
        #             tmp[open] = dp[open + 1]
        #         elif open > 0:
        #             tmp[open] = dp[open - 1]
        #     dp = tmp
        
        # return dp[0]


        # Approach 5: Stack

        # left, star = [], []

        # for i in range(len(s)):
        #     if s[i] == "(":
        #         left.append(i)
        #     elif s[i] == "*":
        #         star.append(i)
        #     else:
        #         if left:
        #             left.pop()
        #         elif star:
        #             star.pop()
        #         else:
        #             return False

        # while left and star:
        #     if left.pop() > star.pop():
        #         return False
        
        # return not left


        # Approach 6: Greedy

        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0