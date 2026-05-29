class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # Approach 1: Recursion

        # def dfs(i, total):
        #     if i >= len(nums):
        #         return target == total

        #     return dfs(i+1, total-nums[i]) + dfs(i+1, total+nums[i])

        # return dfs(0, 0)


        # Approach 2: Dynamic Programming (Top - Down)

        # dp = {}

        # def dfs(i, total):
        #     if i >= len(nums):
        #         return total == target
        #     if (i, total) in dp:
        #         return dp[(i, total)]

        #     dp[(i, total)] = dfs(i+1, total-nums[i]) + dfs(i+1, total+nums[i])
        #     return dp[(i, total)]

        # return dfs(0, 0)


        # Approach 3: Dynamic Programming (Bottom-Up)

        # n = len(nums)
        # dp = [defaultdict(int) for _ in range(n + 1)]
        # dp[0][0] = 1

        # for i in range(n):
        #     for total, count in dp[i].items():
        #         dp[i+1][total - nums[i]] += count
        #         dp[i+1][total + nums[i]] += count

        # return dp[n][target]


        # Approach 4: Dynamic Programming (Space Optimized)

        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            tmp = defaultdict(int)
            for total, count in dp.items():
                tmp[total - nums[i]] += count
                tmp[total + nums[i]] += count
            dp = tmp

        return dp[target]