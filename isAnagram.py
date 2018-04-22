def isAnagram(s, t):
    ht_s = {}
    ht_t = {}
    
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        if not ht_s.get(s[i]):
            ht_s[s[i]] = 1
        else:
            ht_s[s[i]] += 1
        
        if not ht_t.get(t[i]):
            ht_t[t[i]] = 1
        else:
            ht_t[t[i]] += 1

    for key in ht_s:
        if ht_s.get(key) != ht_t.get(key):
            return False
    return True