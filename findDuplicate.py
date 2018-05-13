def findDuplicate(nums):
    low = 0
    high = len(nums) - 1
    mid = (high + low) / 2
    
    while high - low > 1:
        count = 0        
        for n in nums:
            if n > mid and n <= high:
                count += 1
        if count > high - mid:
            low = mid
        else:
            high = mid
        mid = (high + low) / 2
    return high