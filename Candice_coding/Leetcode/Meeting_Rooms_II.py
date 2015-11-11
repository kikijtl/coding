# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# 
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

import heapq


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)
    

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda interval: interval.start)
        n = 0
        hp = []
        for i in xrange(len(intervals)):
            if not hp:
                heapq.heappush(hp, intervals[i].end)
                n += 1
            else:
                if intervals[i].start >= hp[0]:
                    heapq.heappop(hp)
                else:
                     n += 1
                heapq.heappush(hp, intervals[i].end)
        return n


if __name__ == '__main__':
    interval_data = [[0, 30],[5, 10],[15, 20]]
    intervals = []
    for start, end in interval_data:
        intervals.append(Interval(start, end))
    print Solution().minMeetingRooms(intervals)