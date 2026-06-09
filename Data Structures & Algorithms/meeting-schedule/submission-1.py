"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # total_interval = [-1, -1]
        total_interval = -1
        intervals.sort(key=lambda x:x.start)
        # total_interval[0] = intervals[0][0]
        for i in intervals:
            if total_interval == -1:
                # total_interval[0] = i.start
                total_interval = i.end
            else:
                if total_interval > i.start:
                    return False
                total_interval = i.end
        return True