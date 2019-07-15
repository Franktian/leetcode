class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ht = {}
        x = 0
        y = 0
        xd = 0
        yd = 1

        for i in range(len(s)):
            ht[(x, y)] = s[i]

            if numRows == 1:
                xd = 1
                yd = 0
            elif y == numRows - 1:
                xd = 1
                yd = -1
            elif y == 0:
                xd = 0
                yd = 1

            x += xd
            y += yd

        res = ''
        for i in range(numRows + 1):
            for j in range(x + 1):
                if ht.get((j, i)):
                    res += ht[(j, i)]
        
        return res
