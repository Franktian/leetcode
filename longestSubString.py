def longest(string):
    res = ''
    maximum = res

    for c in string:
        if not c in res:
            res += c
            if len(res) > len(maximum):
                maximum = res
        else:
            i = res.index(c)
            res = res[i + 1:] + c

    return maximum
