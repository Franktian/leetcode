def longestCommonPrefix(strs):
    # TODO: Implement Binary Search method
    if len(strs) == 0:
        return ''
    res = strs[0]

    for s in strs:
        common = longestCommonPrefixTwo(s, res)
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
