# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = []
        ends = []

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        used_room = 0
        start = 0
        end = 0

        while start < len(intervals):
            if starts[start] >= ends[end]:
                used_room -= 1
                end += 1

            used_room += 1
            start += 1

        return used_room
