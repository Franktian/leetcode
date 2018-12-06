class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(ums, 0, [], res)
        return res

    def dfs(self, nums, start, subset, res):
        res.append(subset)

        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, subset + [nums[i]], res)
