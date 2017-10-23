"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""
# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        min_rooms, cnt_rooms = 0, 0
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()
        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0

        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1
                min_rooms = max(cnt_rooms, min_rooms)
                s += 1
            else:
                cnt_rooms -= 1
                e += 1
        return min_rooms
