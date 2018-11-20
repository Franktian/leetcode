def mostCommonWord(self, paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    ht = {}
    import re
    paragraph = re.sub('[!?\',;.]', ' ', paragraph)
    p_list = [x.lower() for x in paragraph.split()]

    for p in p_list:
        if not ht.get(p):
            ht[p] = 1
        else:
            ht[p] += 1

    max_word = ""
    freq = 0

    for key, value in ht.iteritems():
        if not key in banned and value >= freq:
            max_word = key
            freq = value
    return max_word
