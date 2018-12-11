def addDigits(num):
    if num < 10:
        return num
    s = sumOfDigit(num)
    return addDigits(s)


def sumOfDigit(num):
    s = 0
    while num != 0:
        s += num % 10
        num /= 10
    return s
