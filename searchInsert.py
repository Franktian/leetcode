def searchInsert(nums, target):
    if target < nums[0] or target == nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    
    index = 0
    for i in range(1, len(nums)):
        if target < nums[i] and target > nums[i - 1]:
            return i
        if target == nums[i]:
            return i