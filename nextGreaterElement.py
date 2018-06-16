def nextGreaterElement(self, findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    ht = {}
    
    for i in range(len(nums)):
        ht[nums[i]] = i
    
    res = []
    
    for n in findNums:
        index = ht[n]
        found = False
        
        if index == len(nums) - 1:
            res.append(-1)
            continue
    
        for i in range(index + 1, len(nums)):
            if nums[i] > n:
                res.append(nums[i])
                found = True
                break
        if not found:
            res.append(-1)
    return res
