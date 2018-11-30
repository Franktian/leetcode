class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = []
        res = []

        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if queue[0] == i - k:
                queue.pop(0)
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res
