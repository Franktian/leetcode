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
