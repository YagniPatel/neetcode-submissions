class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Approach 1: Recursion

        # def dfs(i):
        #     if i >= len(nums) - 1:
        #         return True

        #     end = min(len(nums) - 1, i + nums[i])
        #     for j in range(i + 1, end + 1):
        #         if dfs(j):
        #             return True
        #     return False

        # return dfs(0)


        # Approach 2: Dynamic Programming (Top - Down)

        # dp = {}

        # def dfs(i):
        #     if i == len(nums) - 1:
        #         return True
        #     if i in dp:
        #         return dp[i]

        #     end = min(len(nums) - 1, i + nums[i])
        #     for j in range(i + 1, end + 1):
        #         if dfs(j):
        #             dp[i] = True
        #             return True

        #     dp[i] = False
        #     return False
            
        # return dfs(0)


        # Approach 3: Dynamic Programming (Bottom - Up)

        # dp = [False] * len(nums)
        # dp[-1] = True

        # for i in range(len(nums) - 2, -1, -1):
        #     end = min(len(nums) - 1, i + nums[i])
        #     for j in range(i+1, end + 1):
        #         if dp[j]:
        #             dp[i] = True
        #             break
        
        # return dp[0]


        # Approach 4: Greedy

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0