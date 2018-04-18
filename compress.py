def compress(chars):
    i = 0
    j = 0
    
    while i < len(chars):
        curr = chars[i]
        count = 0

        while i < len(chars) and chars[i] == curr:
            i += 1
            count += 1
        
        chars[j] == curr
        j += 1

        if count != 1:
            for c in str(count):
                chars[j] = c
                j += 1

    return j