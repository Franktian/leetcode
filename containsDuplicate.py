def containsDuplicate(nums):
    dups = {}
    
    for n in nums:
        if not dups.get(n):
            dups[n] = 1
        else:
            return True
    return False