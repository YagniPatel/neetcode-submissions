"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Approach 1: Min Heap

        # intervals.sort(key = lambda x: x.start)
        # minHeap = []

        # for interval in intervals:
        #     if minHeap and minHeap[0] <= interval.start:
        #         heapq.heappop(minHeap)
        #     heapq.heappush(minHeap, interval.end)

        # return len(minHeap)        


        # Approach 2: Sweep Line Algorithm

        # mp = defaultdict(int)
        # for i in intervals:
        #     mp[i.start] += 1
        #     mp[i.end] -= 1

        # pre = 0
        # res = 0
        # for k in sorted(mp.keys()):
        #     pre += mp[k]
        #     res = max(res, pre)

        # return res


        # Approach 3: Two Pointers

        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])

        # s, e = 0, 0
        # count, res = 0, 0

        # while s < len(intervals):
        #     if start[s] < end[e]:
        #         count += 1
        #         s += 1
        #     else:
        #         count -= 1
        #         e += 1
        #     res = max(res, count)

        # return res


        # Approach 4: Greedy

        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))

        time.sort(key = lambda i: (i[0], i[1]))
        
        count, res = 0, 0
        for i in sorted(time):
            count += i[1]
            res = max(res, count)

        return res