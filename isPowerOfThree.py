def isPowerOfThree(n):
    if n < 3:
        return False

    while n != 1:
        if n % 3 != 0:
            return False
        n /= 3
    return True

def getRow(rowIndex):
    if rowIndex == 1:
        return [1]

def getNextRow(row):
    res = [1]
    for i in range(len(lst) - 1):
        res.append(lst[i] + lst[i + 1])
    res.append(1)
    return res