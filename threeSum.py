class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()

        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1

            while i < j:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    i += 1
                    j -= 1
                elif s > 0:
                    j -= 1
                else:
                    i += 1

        return map(list, res)
