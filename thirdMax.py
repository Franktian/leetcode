import sys
def thirdMax(nums):
    max_three = [-sys.maxsize]

    for n in nums:
        m = min(max_three) or -sys.maxsize
        if n > m and not n in max_three:
            max_three.append(n)
        if len(max_three) > 3:
            max_three.remove(m)

    if -sys.maxsize in max_three:
        max_three.remove(-sys.maxsize)

    if len(max_three) < 3:
        return max(max_three)

    return min(max_three)

def kMax(nums, k):
    max_k = [-sys.maxsize]

    for n in nums:
        m = min(max_k)
        if n > m:
            max_k.append(n)
        if len(max_k) > k:
            max_k.remove(m)

    if -sys.maxsize in max_k:
        max_k.remove(-sys.maxsize)

    return min(max_k)
