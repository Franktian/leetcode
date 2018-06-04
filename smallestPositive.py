def smallest(A):
    
    ht = {}
    max_element = max(A)

    if max_element < 0:
        return 1

    for i in A:
        if i not in ht:
            ht[i] = 1

    for i in range(1, max_element + 1):
        if i not in ht:
            return i

    return max_element + 1