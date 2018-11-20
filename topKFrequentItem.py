def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    ht = {}

    for n in nums:
        if n not in ht:
            ht[n] = 1
        else:
            ht[n] += 1

    heap = []
    from heapq import heappush, heappop

    for key, value in ht.iteritems():
        item = (-value, key)
        heappush(heap, item)

    res = []
    for i in range(k):
        item = heappop(heap)
        res.append(item[1])
    return res
