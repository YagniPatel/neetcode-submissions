class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Approach 1: Sorting

        # intervals.sort(key = lambda pair: pair[0])
        # res = [intervals[0]]

        # for start, end in intervals:
        #     if res[-1][1] >= start:
        #         res[-1][0] = min(res[-1][0], start)
        #         res[-1][1] = max(res[-1][1], end)
        #     else:
        #         res.append([start, end])

        # return res


        # Approach 2: Sweep Line Algorithm

        # mp = defaultdict(int)
        # for start, end in intervals:
        #     mp[start] += 1
        #     mp[end] -= 1

        # res = []
        # interval = []
        # have = 0
        # for i in sorted(mp):
        #     if not interval:
        #         interval.append(i)

        #     have += mp[i]
        #     if have == 0:
        #         interval.append(i)
        #         res.append(interval)
        #         interval = []

        # return res           


        # Approach 3: Greedy

        max_start = max(interval[0] for interval in intervals)
        mp = [0] * (max_start + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        interval_start = -1
        have = -1
        res = []
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(have, mp[i] - 1)

            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            res.append([interval_start, have])

        return res