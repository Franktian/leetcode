def findAllPairs(lst):
    ht = {}
    res = []

    for i in lst:
        ht[i] = 1
        diff = 100 - i
        if ht.get(diff):
            res.append([i, diff])

    return res
