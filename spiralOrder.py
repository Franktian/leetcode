def spiralOrder(matrix):
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1
    
    ret = []
    if not matrix:
        return ret
    
    while left < right and top < bottom:
        for i in range(left, right):
            ret.append(matrix[top][i])

        for i in range(top, bottom):
            ret.append(matrix[i][right])

        for i in range(right, left, -1):
            ret.append(matrix[bottom][i])

        for i in range(bottom, top, -1):
            ret.append(matrix[i][left])
        left += 1
        right -= 1
        top += 1
        bottom -= 1

    if left == right and top == bottom:
        ret.append(matrix[left][top])
    elif top == bottom:
        for i in range(left, right + 1):
            ret.append(matrix[top][i])
    elif left == right:
        for i in range(top, bottom + 1):
            ret.append(matrix[i][left])
    return ret
