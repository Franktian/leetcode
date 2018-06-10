def smallestDistancePair(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    res = []
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            res.append(abs(nums[i] - nums[j]))

    res.sort()
    print res

    return res[k - 1]