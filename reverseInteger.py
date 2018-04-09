def reverse(x):
    if x >= 0:
        return reverseInt(x)
    return -reverseInt(-x)
def reverseInt(x):
    s = str(x)
    l = len(s)
    r = ''
    for d in range(0, l):
        r += s[l - d - 1]
    if int(r) > (2 ** 31 - 1):
        return 0
    return int(r)
