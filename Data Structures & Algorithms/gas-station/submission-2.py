class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Approach 1: Brute Force

        # n = len(gas)
        # for i in range(n):
        #     tank = gas[i] - cost[i]
        #     if tank < 0:
        #         continue

        #     j = (i + 1) % n
        #     while j != i:
        #         tank += gas[j] - cost[j]
        #         if tank < 0:
        #             break
        #         j = (j + 1) % n

        #     if j == i:
        #         return i
        
        # return -1


        # Approach 2: Two Pointers

        # n = len(gas)
        # start, end = len(gas) - 1, 0
        # tank = gas[start] - cost[start]
        # while start > end:
        #     if tank > 0:
        #         tank += gas[end] - cost[end]
        #         end += 1
        #     else:
        #         start -= 1
        #         tank += gas[start] - cost[start]

        # return start if tank >= 0 else -1


        # Approach 3: Greedy

        if sum(gas) < sum(cost): return -1

        pre = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                pre = i + 1
                tank = 0

        return pre