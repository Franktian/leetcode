def longestCommonSubstring(s1, s2):
    m = len(s1)
    n = len(s2)
    L = [ [ 0 for i in range(n)] for j in range(m)]
    z = 0
    res = []

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    L[i][j] = 1
                else:
                    L[i][j] = L[i - 1][j - 1] + 1

                if L[i][j] > z:
                    z = L[i][j]
                    res = []
                    res.append(s1[i-z+1:i+1])
                elif L[i][j] == z:
                    res.append(s1[i-z+1:i+1])

    return res