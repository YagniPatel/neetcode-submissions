class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Approach 1: Linear Search

        # res = []
        # i = 0
        # n = len(intervals)

        # while i < n and intervals[i][1] < newInterval[0]:
        #     res.append(intervals[i])
        #     i += 1
        
        # while i < n and intervals[i][0] <= newInterval[1]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # res.append(newInterval)
        
        # while i < n:
        #     res.append(intervals[i])
        #     i += 1

        # return res


        # Approach 2: Binary Search

        # l, r = 0, len(intervals) - 1
        # while l <= r:
        #     m = l + (r - l) // 2

        #     if intervals[m][0] < newInterval[0]:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # intervals.insert(l, newInterval)

        # res = []
        # for start, end in intervals:
        #     if not res or res[-1][1] < start:
        #         res.append([start, end])
        #     else:
        #         res[-1][0] = min(res[-1][0], start)
        #         res[-1][1] = max(res[-1][1], end)

        # return res


        # Approach 3: Greedy

        res = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res