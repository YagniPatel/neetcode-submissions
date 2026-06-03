class Solution:
    def jump(self, nums: List[int]) -> int:

        # Approach 1: Recursion

        # def dfs(i):
        #     if i >= len(nums) - 1:
        #         return 0

        #     res = float('inf')
        #     for j in range(i + 1, i + nums[i] + 1):
        #         res = min(res, 1 + dfs(j))
        #     return res

        # return dfs(0)


        # Approach 2: Dynamic Programming (Top-Down)

        # dp = {}

        # def dfs(i):
        #     if i >= len(nums) - 1:
        #         return 0
        #     if i in dp:
        #         return dp[i]

        #     res = float('inf')
        #     for j in range(i + 1, i + nums[i] + 1):
        #         res = min(res, 1 + dfs(j))
        #     dp[i] = res
        #     return res
            
        # return dfs(0)


        # Approach 3: Dynamic Programming (Bottom - Up)
        
        # dp = [float('inf')] * len(nums)
        # dp[-1] = 0
        # for i in range(len(nums) - 2, -1, -1):            
        #     for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
        #         dp[i] = min(dp[i], 1 + dp[j])

        # return dp[0]


        # Approach 4: Breadth First Search (Greedy)

        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            res += 1
            mx = 0
            for i in range(l, r+1):
                mx = max(mx, i + nums[i])
            l = r + 1
            r = mx

        return res