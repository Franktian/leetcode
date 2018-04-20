import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()