"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]

        starts.sort()
        ends.sort()

        max_days = 0
        days = 0

        start_ptr = 0
        end_ptr = 0
        while start_ptr < len(starts):
            if starts[start_ptr] < ends[end_ptr]:
                start_ptr += 1
                days += 1
                max_days = max(max_days, days)
            else:
                end_ptr += 1
                days -= 1

        return max_days




