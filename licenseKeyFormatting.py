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
