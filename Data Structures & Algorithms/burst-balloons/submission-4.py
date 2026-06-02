class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # Approach 1: Recursion

        # def dfs(nums):
        #     if len(nums) == 2:
        #         return 0
            
        #     mx = 0
        #     for i in range(1, len(nums)-1):
        #         coins = nums[i-1] * nums[i] * nums[i+1]
        #         coins += dfs(nums[:i] + nums[i+1:])
        #         mx = max(mx, coins)
        #     return mx
            
        # nums.insert(0, 1)
        # nums.append(1)
        # return dfs(nums)


        # Approach 2: Dynamic Programming (Top - Down)

        # dp = {}
        # def dfs(l, r):
        #     if l > r:
        #         return 0
        #     if (l, r) in dp:
        #         return dp[(l, r)]

        #     mx = 0
        #     for i in range(l, r+1):
        #         coins = nums[l-1] * nums[i] * nums[r+1]
        #         coins += dfs(l, i-1) + dfs(i+1, r)
        #         mx = max(coins, mx)

        #     dp[(l, r)] = mx
        #     return mx

        # nums = [1] + nums + [1]
        # return dfs(1, len(nums) - 2)


        # Approach 3: Dynamic Programming (Bottom - Up)

        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n+2) for _ in range(n+2)]

        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for i in range(l, r+1):
                    coins = nums[l-1] * nums[i] * nums[r+1]
                    coins += dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]