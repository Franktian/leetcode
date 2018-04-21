def selfDividingNumbers(left, right):
    res = []
    for i in range(left, right + 1):
        if isSelf(i):
            res.append(i)
    return res

def isSelf(num):
    self = num
    while num > 0:
        digit = num % 10
        if digit == 0:
            return False
        if self % digit != 0:
            return False
        num /= 10
    return True