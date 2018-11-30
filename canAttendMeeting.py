class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        
        if len(intervals) < 2:
            return True
        
        intervals.sort(cmp = lambda x, y : x.start - y.start)
        
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
