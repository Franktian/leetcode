def removeDuplicates(nums):
    if not nums:
        return 0
    
    prev = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[prev]:
            prev += 1
            nums[prev] = nums[i]
    return prev + 1
