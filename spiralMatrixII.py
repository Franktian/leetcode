class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []

        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        res = [[0 for x in range(n)] for x in range(n)]
        count = 1

        while left < right and top < bottom:
            for i in range(left, right):
                res[top][i] = count
                count += 1

            for i in range(top, bottom):
                res[i][right] = count
                count += 1

            for i in range(right, left, -1):
                res[bottom][i] = count
                count += 1

            for i in range(bottom, top, -1):
                res[i][left] = count
                count += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if n % 2 == 1:
            res[left][top] = count
        return res