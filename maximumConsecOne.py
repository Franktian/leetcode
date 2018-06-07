def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    res = 0
    curr = 0
    
    for n in nums:
        if n == 1:
            curr += 1
        else:
            curr = 0

        if curr >= res:
                res = curr
    return res
