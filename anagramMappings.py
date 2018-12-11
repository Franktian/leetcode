def anagramMappings(A, B):
    ht = {}

    for i in range(len(B)):
        ht[B[i]] = i

    res = []

    for n in A:
        res.append(ht.get(n))

    return resadsfasdf
