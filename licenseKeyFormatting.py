def licenseKeyFormatting(self, S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    rev = S[::-1]
    res = ''
    count = 0
    
    for s in rev:
        if s != '-':
            if count < K:
                res += s.upper()
                count += 1
            else:
                res += '-' + s.upper()
                count = 1
    
    return res[::-1]

def boldWords(S, words):
    N = len(S)
    masks = [False] * N
    
    for i in range(N):
        prefix = S[i:]
        for w in words:
            if prefix.startswith(w):
                for j in range(i, min(i + len(w), N)):
                    masks[j] = True

    res = []
    for i in range(N):
        if masks[i] and (i == 0 or not masks[i - 1]):
            res.append('<b>')
        res.append(S[i])
        if masks[i] and (i == N - 1 or not masks[i + 1]):
            res.append('</b>')

    return ''.join(res)

def trap(height):
    if not height:
        return 0
    
    l = len(height)
    left_max = [0] * l
    right_max = [0] * l
    left_max[0] = height[0]

    i = 1
    while i < l:
        left_max[i] = max(left_max[i - 1], height[i])
        i += 1

    right_max[l - 1] = height[l - 1]
    j = l - 2
    while j >= 0:
        right_max[j] = max(right_max[j + 1], height[j])
        j -= 1

    print left_max
    print right_max

    res = 0
    for k in range(l):
        res += min(left_max[k], right_max[k]) - height[k]
    return res
