def reverseStr(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    res = list(s)

    for i in range(0, len(s), 2 * k):
        x = i
        y = min(x + k - 1, len(s) - 1)

        while x < y:
            res[x], res[y] = res[y], res[x]
            x += 1
            y -= 1

    return "".join(res)
