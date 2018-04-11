def getSum(a, b):
    while b != 0:
        print b
        carry = a & b # And
        a = a ^ b     # XOR
        b = carry << 1
    return a

def getSumR(a, b):
    if not b:
        return a
    return getSum(a ^ b, (a & b) << 1)