def threeSum(nums):
    nums.sort()
    res = set()
    
    for k in range(len(nums)):
        target = -nums[k]

        i = k + 1
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                res.add((nums[k], nums[i], nums[j]))
                i += 1
                j -= 1
            elif nums[i] + nums[j] > 0:
                j -= 1
            else:
                i += 1
    return map(list, res)
