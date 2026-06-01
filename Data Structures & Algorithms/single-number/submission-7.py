class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Approach 1: Brute Force

        # for i in range(len(nums)):
        #     flag = True
        #     for j in range(len(nums)):
        #         if i != j and nums[i] == nums[j]:
        #             flag = False
        #             break
        #     if flag:
        #         return nums[i]

        
        # Approach 2: Hash Set

        # s = set()

        # for num in nums:
        #     if num in s:
        #         s.remove(num)
        #     else:
        #         s.add(num)

        # return list(s)[0]


        # Approach 3: Sorting

        # nums.sort()

        # for i in range(0, len(nums)-2, 2):
        #     if nums[i] != nums[i+1]:
        #         return nums[i]

        # return nums[-1]


        # Approach 4: Bit Manipulation

        res = 0
        for num in nums:
            res = res ^ num
        return res