def removeDuplicates(nums):
    if not nums:
        return 0
    
    prev = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[prev]:
            prev += 1
            nums[prev] = nums[i]
    return prev + 1

def removeElement(nums, val):
    if not nums:
        return 0
    if len(nums) == 1:
        if nums[0] == val:
            nums.pop()
            return 0
        else:
            return 1
    prev = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[prev] = nums[i]
            prev += 1
    return prev
