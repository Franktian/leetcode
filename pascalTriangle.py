def generate(numRows):
    if numRows == 0:
        return []

    if numRows == 1:
        return [[1]]
    
    triangle = [[1]]

    for i in range(2, numRows + 1):
        nextRow = getNextRow(triangle[-1])
        triangle.append(nextRow)
    return triangle

def getNextRow(row):
    res = [1]
    for i in range(len(row) - 1):
        res.append(row[i] + row[i + 1])
    res.append(1)
    return res