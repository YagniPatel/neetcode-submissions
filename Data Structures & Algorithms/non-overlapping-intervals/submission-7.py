class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Approach 1: Recursion

        # intervals.sort()

        # def dfs(i, pre):
        #     if i >= len(intervals):
        #         return 0

        #     res = dfs(i + 1, pre)
        #     if pre == -1 or (intervals[pre][1] <= intervals[i][0]):
        #         res = max(res, 1 + dfs(i + 1, i))

        #     return res

        # return len(intervals) - dfs(0, -1)


        # Approach 2: Dynamic Programming (Top-Down)

        # mp = {}
        # intervals.sort(key = lambda i: i[1])

        # def dfs(i):
        #     if i in mp:
        #         return mp[i]
            
        #     res = 1
        #     for j in range(i + 1, len(intervals)):
        #         if intervals[i][1] <= intervals[j][0]:
        #             res = max(res, 1 + dfs(j))

        #     mp[i] = res
        #     return res

        # return len(intervals) - dfs(0)


        # Approach 3: Dynamic Programming (Bottom-Up)

        # intervals.sort(key = lambda i: i[1])
        # mp = [0] * len(intervals)

        # for i in range(len(intervals)):
        #     mp[i] = 1
        #     for j in range(i):
        #         if intervals[j][1] <= intervals[i][0]:
        #             mp[i] = max(mp[i], 1 + mp[j])

        # return len(intervals) - max(mp)


        # Approach 4: Dynamic Programming (Binary Search)

        # intervals.sort(key = lambda i: i[1])
        # mp = [0] * len(intervals)
        # mp[0] = 1

        # for i in range(1, len(intervals)):
        #     l, r = 0, i

        #     while l < r:
        #         m = l + (r - l) // 2

        #         if intervals[m][1] <= intervals[i][0]:
        #             l = m + 1
        #         else:
        #             r = m

        #     if l == 0:
        #         mp[i] = mp[i-1]
        #     else:
        #         mp[i] = max(mp[i-1], 1 + mp[l-1])

        # return len(intervals) - mp[-1]


        # Approach 5: Greedy (Sort By Start)

        # intervals.sort()
        # res = 0
        # pre = intervals[0][1] if intervals else 0

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] >= pre:
        #         pre = intervals[i][1]
        #     else:
        #         res += 1
        #         pre = min(pre, intervals[i][1])

        # return res


        # Approach 6: Greedy (Sort By End)

        intervals.sort(key = lambda i: i[1])
        res = 0
        pre = intervals[0][1] if intervals else 0

        for start, end in intervals[1:]:
            if start >= pre:
                pre = end
            else:
                res += 1
                
        return res