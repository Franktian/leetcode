def intersection(nums1, nums2):
    ht = {}
    
    for n in nums1:
        if not ht.get(n):
            ht[n] = 1
        else:
            ht[n] += 1
    
    res = []
    
    for n in nums2:
        if ht.get(n) and not n in res:
            res.append(n)
            
    return res
