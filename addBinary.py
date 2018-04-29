def addBinary(a, b):
    sa = []
    sb = []
    
    for i in a:
        sa.append(int(i))
    
    for j in b:
        sb.append(int(j))
        
    res = ""
    carry = 0
    
    while sa or sb:
        if sa:
            x = sa.pop()
        else:
            x = 0

        if sb:
            y = sb.pop()
        else:
            y = 0

        curr = x + y + carry
        
        if curr > 1:
            curr -= 2
            carry = 1
        else:
            carry = 0
        
        res += str(curr)
    
    if carry == 1:
        res += "1"
    
    return res[::-1]

