# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# 
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)
    
    
class Solution(object):
    def canAttendMeetings(self, intervals):
        '''
        :type intervals: List[Interval]
        :rtype: bool
        '''
        intervals.sort(key=lambda interval: interval.start)
        for i in xrange(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

if __name__ == '__main__':
    intervals = [Interval(4, 10), Interval(2, 20)]
    print Solution().canAttendMeetings(intervals)