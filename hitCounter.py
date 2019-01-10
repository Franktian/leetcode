class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = collections.defaultdict(int)

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.hits[timestamp] += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        counts = 0
        start = timestamp - 300 if timestamp - 300 > 0 else 0
        
        for i in range(start, timestamp + 1):
            counts += self.hits[i + 1]

        return counts
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)