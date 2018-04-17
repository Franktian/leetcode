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


def intersection2(nums1, nums2):
    ht1 = {}
    ht2 = {}

    for n in nums1:
        if not ht1.get(n):
            ht1[n] = 1
        else:
            ht1[n] += 1

    res = []
    for n in nums2:
        if not ht2.get(n):
            ht2[n] = 1
        else:
            ht2[n] += 1

        if ht1.get(n) and ht2.get(n) <= ht1.get(n):
            res.append(n)


    return res
