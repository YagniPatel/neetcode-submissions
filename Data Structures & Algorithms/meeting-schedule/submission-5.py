"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Approach 1: Brute Force

        # n = len(intervals)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if max(intervals[i].start, intervals[j].start) < min(intervals[i].end, intervals[j].end):
        #             return False
        
        # return True


        # Approach 2: Sorting

        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True