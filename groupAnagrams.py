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


def binary(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (high + low) / 2
        print mid

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1