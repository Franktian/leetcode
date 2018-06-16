def nextClosestTime(time):
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])
    current = hour * 60 + minute

    chars = {}
    for c in time:
        if c not in chars and c != '-':
            chars[c] = 1

    i = 0
    while True:
        current = (current + 1) % 1440
        digits = [current / 60 / 10, current / 60 % 10, current % 60 / 10, current % 60 % 10]
        counts = 0
        
        for d in digits:
            if str(d) in chars:
                counts += 1

        if counts == 4:
            return "{}{}:{}{}".format(digits[0], digits[1], digits[2], digits[3])

def replace(roots):
    import collections
    _trie = lambda: collections.defaultdict(_trie)
    trie = _trie()
    END = True
    for root in roots:
        cur = trie
        for letter in root:
            cur = cur[letter]
        cur[END] = root

    print trie.values().pop()
