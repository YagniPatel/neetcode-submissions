class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Approach 1: Brute Force

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # Approach 2: Sorting

        # a = []
        # for i, num in enumerate(nums):
        #     a.append([num, i])

        # a.sort()
        # i, j = 0, len(nums)-1

        # while i<j:
        #     cur = a[i][0] + a[j][0]
        #     if cur == target:
        #         return [min(a[i][1], a[j][1]), max(a[i][1], a[j][1])]
        #     elif cur < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return []

        # Approach 3: Hash Map (two pass)

        # ind = {}

        # for i, num in enumerate(nums):
        #     ind[num] = i

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in ind and ind[diff] != i:
        #         return [i, ind[diff]]
        # return []

        # Approach 4: Hash Map (one pass)

        ind = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in ind and ind[diff] != i:
                return [ind[diff], i]
            ind[num] = i
        return [] 