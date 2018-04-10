def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]

    res = strs[0]
    for i in range(len(strs) - 1):
        for j in range(i + 1, len(strs)):
            common = longestCommonPrefixTwo(strs[i], strs[j])
            
            if len(common) <= len(res):
                res = common
    return res

def longestCommonPrefixTwo(s1, s2):
    l = min(len(s1), len(s2))
    
    common = ''
    for i in range(l):
        if s1[i] == s2[i]:
            common += s1[i]
        else:
            break
    return common
