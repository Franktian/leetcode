def trailingZeroes(n):
    nn = n
    for i in range(1, n):
        nn *= i

    res = 0
    while nn > 0 and nn % 10 == 0:
        res += 1
        nn /= 10
    return res