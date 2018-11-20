def partitionLabels(self, S):
    """
    :type S: str
    :rtype: List[int]
    """
    lasts = {}

    for i in range(len(S)):
        lasts[S[i]] = i

    res = []
    start = end = 0

    for i in range(len(S)):
        end = max(end, lasts.get(S[i]))

        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res
