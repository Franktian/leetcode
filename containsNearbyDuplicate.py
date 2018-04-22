def containsNearbyDuplicate(nums, k):
    ht = {}
    
    for i in range(len(nums)):
        if not ht.get(nums[i]):
            ht[nums[i]] = [i]
        else:
            ht[nums[i]].append(i)
    
    print ht
    for key in ht:
        if len(ht[key]) > 1 and overMaxDifference(ht[key], k):
            return True
    return False

def overMaxDifference(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) <= k:
                return True
    return False