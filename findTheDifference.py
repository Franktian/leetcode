def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ht_s = {}
    ht_t = {}
    
    for i in s:
        if not ht_s.get(i):
            ht_s[i] = 1
        else:
            ht_s[i] += 1
    
    for j in t:
        if not ht_t.get(j):
            ht_t[j] = 1
        else:
            ht_t[j] += 1
    print ht_s
    print ht_t