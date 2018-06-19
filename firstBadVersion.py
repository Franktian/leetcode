def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    low = 1
    high = n
    
    while low < high:
        mid = (low + high) // 2
        
        isBad = isBadVersion(mid)
        
        if isBad:
            high = mid
        else:
            low = mid + 1
    
    return low
