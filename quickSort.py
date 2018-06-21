def quickSort(lst):
    if len(lst) <= 1:
        return lst
    
    less = []
    equal = []
    greater = []
    
    pivot = lst[0]
    
    for n in lst:
        if n < pivot:
            less.append(n)
        elif n > pivot:
            greater.append(n)
        else:
            equal.append(n)
    
    return quickSort(less) + equal + quickSort(greater)

def distance(s, t):
    m = len(s)
    n = len(t)
    
    if abs(m - n) > 1:
        return False
    
    edits = 0
    i = j = 0
    while i < m and j < n:
        if s[i] != s[j]:
            print "Not equal"
            if edits == 1:
                return False
            else:
                if m == n:
                    i += 1
                    j += 1
                elif m > n:
                    i += 1
                else:
                    j += 1
                edits += 1
        else:
            i += 1
            j += 1
    
    if m != n:
        edits += 1
    print edits
    return edits == 1


def firstMissingPositive(nums):
    
    for i in range(len(nums)):
        while nums[i] >= 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
            swap = nums[i] - 1
            nums[i], nums[swap] = nums[swap], nums[i]

    print nums
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1

def countAndSay(n):
    if n == 1:
        return "1"
    
    res = countAndSay(n - 1)
    return count(res)

def count(s):
    count = 1
    i = 1
    res = ""
    
    while i < len(s):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res += str(count) + s[i - 1]
            count = 1
        i += 1
    
    res += str(count) + s[-1]
    return res