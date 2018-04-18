def mergeSorted(num1, m, num2, n):
    while m > 0 and n > 0:
        if num1[m - 1] > num2[n - 1]:
            num1[m + n - 1] = num1[m - 1]
            m -= 1
        else:
            num1[m + n - 1] = num2[n - 1]
            n -= 1

    if n > 0:
        num1[:n] = num2[:n]