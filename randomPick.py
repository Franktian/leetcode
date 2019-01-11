class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indexes = collections.defaultdict(list)
        for i in range(len(nums)):
            self.indexes[nums[i]].append(i)


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indexes = self.indexes[target]
        from random import randint
        rand = randint(0, len(indexes) - 1)
        return indexes[rand]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)