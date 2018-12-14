class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_copied = nums[:]
        nums_copied.sort()
        
        end = 0
        start = len(nums) - 1
        
        for i in range(len(nums)):
            if nums[i] != nums_copied[i]:
                end = max(end, i)
                start = min(start, i)

        return end - start + 1 if end - start > 0 else 0
