class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Appraoch 1: Brute Force

        # res = nums[0]
        # for i in range(len(nums)):
        #     cur = 0
        #     for j in range(i, len(nums)):
        #         cur += nums[j]
        #         res = max(res, cur)
        # return res


        # Approach 2: Recursion

        # def dfs(i, flag):
        #     if i == len(nums) - 1:
        #         return max(0, nums[i]) if flag else nums[i]
        #     if flag:
        #         return max(0, nums[i] + dfs(i+1, flag))
        #     else:
        #         return max(dfs(i+1, flag), nums[i] + dfs(i+1, not flag))

        # return dfs(0, False)


        # Approach 3: Dynamic Programming (Top - Down)

        # dp = {}
        
        # def dfs(i, flag):
        #     if i == len(nums) - 1:
        #         return max(0, nums[i]) if flag else nums[i]
        #     if (i, flag) in dp:
        #         return dp[(i, flag)]

        #     if flag:
        #         dp[(i, flag)] = max(0, nums[i] + dfs(i+1, flag))
        #     else:
        #         dp[(i, flag)] = max(dfs(i+1, flag), nums[i] + dfs(i+1, not flag))

        #     return dp[(i, flag)]

        # return dfs(0, False)


        # Approach 4: Dynamic Programming (Bottom - Up)

        # n = len(nums)
        # dp = [[0] * 2 for _ in range(n)]
        # dp[n-1][0] = nums[-1]
        # dp[n-1][1] = nums[-1]

        # for i in range(n - 2, -1, -1):
        #     dp[i][1] = max(nums[i], nums[i] + dp[i+1][1])
        #     dp[i][0] = max(dp[i+1][0], dp[i][1])

        # return dp[0][0]


        # Approach 5: Dynamic Programming (Space Optimized)

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])

        # return max(dp)


        # Approach 6: Kandane's Algorithm

        # cur = 0
        # mx = nums[0]
        # for num in nums:
        #     cur = max(cur, 0)
        #     cur += num
        #     mx = max(mx, cur)

        # return mx


        # Approach 7: Divide and Conquer

        def dfs(l, r):
            if l > r:
                return -float('inf')

            m = l + (r-l) // 2

            left = 0
            cur = 0
            for i in range(m-1, l-1, -1):
                cur += nums[i]
                left = max(left, cur)

            right = 0
            cur = 0
            for i in range(m+1, r+1):
                cur += nums[i]
                right = max(right, cur)

            return max(dfs(l, m-1), dfs(m+1, r), left + nums[m] + right)

        return dfs(0, len(nums) - 1)


        # Optimized

        # t = f = nums[-1]
        # for i in range(len(nums) - 2, -1, -1):
        #     t = max(nums[i], nums[i] + t)
        #     f = max(f, t)

        # return f