class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row,col,width=len(matrix)-1,0,len(matrix[0])
        while row>=0 and col<width:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                row=row-1
            else:
                col=col+1
        return False