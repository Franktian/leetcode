def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    i = 0
    j = len(s) - 1
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    sl = []
    for c in s:
        sl.append(c)
    
    while i < j:
        while i < j and sl[i].lower() not in vowels:
            i += 1
        while i < j and sl[j].lower() not in vowels:
            j -= 1
        sl[i], sl[j] = sl[j], sl[i]
        i += 1
        j -= 1
    return ''.join(sl)
