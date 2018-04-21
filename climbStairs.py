def climbStairs(n):
    if n < 3:
        return n
    
    f1 = 1
    f2 = 2
    
    for i in range(3, n + 1):
        f0 = f1 + f2
        f1 = f2
        f2 = f0
    return f2

def test():
    for i in range(8):
        print i