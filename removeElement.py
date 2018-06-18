def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    res = 0
    i = 0
    
    while i < len(nums):
        if nums[i] != val:
            res += 1
        else:
            j = i + 1
            while j < len(nums):
                if nums[j] != val:
                    res += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                else:
                    j += 1
        i += 1
    print nums
    return res