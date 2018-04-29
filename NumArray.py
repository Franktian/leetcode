def generateSumArray(lst):
    
    res = [0 for _ in range(len(lst) + 1)]
    
    for i in range(len(lst)):
        res[i + 1] = res[i] + lst[i]
    
    return res