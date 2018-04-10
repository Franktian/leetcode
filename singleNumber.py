def singleNumber(nums):
    res = {}
    for num in nums:
        if not res.get(num):
            res[num] = 1
        else:
            res[num] += 1
    
    for key, value in res.iteritems():
        if value == 1:
            return key
