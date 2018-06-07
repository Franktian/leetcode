def maximumProduct(nums):
    min_1 = sys.maxsize
    min_2 = sys.maxsize
    max_1 = -sys.maxsize
    max_2 = -sys.maxsize
    max_3 = -sys.maxsize

    for n in nums:
        if n <= min_1:
            min_2 = min_1
            min_1 = n
        elif n <= min_2:
            min_2 = n
    
        if n >= max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = n
        elif n >= max_2:
            max_3 = max_2
            max_2 = n
        elif n >= max_3:
            max_3 = n

    return max(min_1 * min_2 * max_1, max_3 * max_2 * max_1)
