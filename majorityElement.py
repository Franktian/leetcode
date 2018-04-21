def majorityElement(nums):
    ht = {}
    
    for n in nums:
        if not ht.get(n):
            ht[n] = 1
        else:
            ht[n] += 1
    
    maj = nums[0]
    
    for key in ht:
        if ht[key] > ht[maj]:
            maj = key
    return maj
