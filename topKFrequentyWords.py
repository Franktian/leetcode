class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ht = collections.defaultdict(int)

        for w in words:
            ht[w] += 1

        from heapq import heappush, heappop

        hp = []

        for key, value in ht.iteritems():
            heappush(hp, (-value, key))

        res = []
        for i in range(k):
            res.append(heappop(hp)[1])

        return res
