class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.st = []
        self.sum = 0.0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.st.append(val)
        self.sum += val

        if len(self.st) > self.size:
            self.sum -= self.st.pop(0)

        return self.sum / len(self.st)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)