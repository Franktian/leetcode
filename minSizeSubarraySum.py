def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    min_length = len(nums) + 1
    
    i = j = 0
    
    sub_s = 0
    
    while j < len(nums):
        sub_s += nums[j]
        
        while sub_s >= s:
            min_length = min(min_length, j - i + 1)
            sub_s -= nums[i]
            i += 1
        j += 1
    
    if min_length != len(nums) + 1:
        return min_length
    return 0
