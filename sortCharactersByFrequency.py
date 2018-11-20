def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    ht1 = defaultdict(int)
    ht2 = defaultdict(list)
    freq = []

    for c in s:
        ht1[c] += 1

    for key, value in ht1.iteritems():
        if not ht2.get(value):
            freq.append(value)
        ht2[value].append(key)

    freq.sort()
    freq.reverse()

    res = ''
    for f in freq:
        item = ht2.get(f)
        for i in item:
            res += i * f
    return res
