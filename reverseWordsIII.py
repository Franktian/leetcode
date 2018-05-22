def reverseWord(s):
    res = []
    words = s.split()
    
    for w in words:
        res.append(reverse(w))
    
    return ' '.join(res)

def reverse(s):
    l = len(s)
    
    if l <= 1:
        return s
    
    left = s[:l / 2]
    right = s[l / 2:]
    
    return reverse(right) + reverse(left)
