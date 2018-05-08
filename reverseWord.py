def reverseWords(s):
    lst = s.split()    
    output = reverseArray(lst)
    return ' '.join(output).strip()

def reverseArray(lst):
    if len(lst) < 2:
        return lst

    l = len(lst)
    left = lst[:l / 2]
    right = lst[l / 2:]

    return reverseArray(right) + reverseArray(left)
