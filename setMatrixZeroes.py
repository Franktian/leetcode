def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    rows = {}
    cols = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows[i] = 1
                cols[j] = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rows.get(i) or cols.get(j):
                matrix[i][j] = 0
