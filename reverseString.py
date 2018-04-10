def reverseString(s):
    res = ''
    for i in range(len(s)):
        #res += s[len(s) - i - 1]
        print s[i]
        print s[len(s) - i - 1]
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    return res

def reverse(s):
    l = len(s)
    if s == "":
        return ""

    if l == 1:
        return s
    
    x = s[l / 2:]
    y = s[:l / 2]
    return reverse(x) + reverse(y)
