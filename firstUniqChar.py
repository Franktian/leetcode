def firstUniqChar(s):
    ht = {}

    for i in range(len(s)):
        if not ht.get(s[i]):
            ht[s[i]] = {
                'i': i,
                'count': 1
            }
        else:
            ht[s[i]]["count"] += 1
    
    m_index = len(s)
    
    for key, value in ht.iteritems():
        if value["count"] == 1 and value["i"] <= m_index:
            m_index = value["i"]

    if m_index == len(s):
        return -1
    return m_index
