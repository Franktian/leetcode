class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        from heapq import *
        hp = []
        result = []
        for coord in points:
            x = coord[0]
            y = coord[1]
            heappush(hp, (x**2 + y**2, [x, y]))

        for i in range(K):
            item = heappop(hp)
            result.append(item[1])

        return result
