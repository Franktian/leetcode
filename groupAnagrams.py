def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    ans = collections.defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()


def binary(nums):
    l = 0
    r = len(nums) - 1
    
    while l < r:
        m = (l + r) // 2
        
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]