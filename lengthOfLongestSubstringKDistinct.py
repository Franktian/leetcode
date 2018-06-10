def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    max_length = 0
    ht = {}

    l = r = 0

    while r < len(s):
        if s[r] not in ht:
            ht[s[r]] = 1
        else:
            ht[s[r]] += 1
        
        while len(ht) > k:
            ht[s[l]] -= 1
            
            if ht[s[l]] == 0:
                ht.pop(s[l])
            l += 1
        
        max_length = max(max_length, r - l + 1)
        r += 1
    
    return max_length
