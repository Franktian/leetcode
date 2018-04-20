def countAndSay(n):
    if n == 1:
        return "1"

    r = countAndSay(n - 1)

    res = count(r)
    return res


def count(s):
    count = 1
    i = 1
    res = ""

    while i < len(s):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res += str(count)
            res += s[i - 1]
            count = 1
        i += 1

    res += str(count)
    res += s[-1]
    return res