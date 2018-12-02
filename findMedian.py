from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.maxHeap, (-num, num))

        top = heappop(self.maxHeap)

        heappush(self.minHeap, (-top[0], top[1]))

        if len(self.maxHeap) < len(self.minHeap):
            top = heappop(self.minHeap)
            heappush(self.maxHeap, (-top[0], top[1]))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0][1]

        return (self.minHeap[0][1] + self.maxHeap[0][1]) / 2.0
