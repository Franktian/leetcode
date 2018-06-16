def shareCommonLetter(word1, word2):
    ht = {}
    
    for w in word1:
        ht[w] = 1
    
    print ht
    
    for w in word2:
        if w in ht:
            return True
    return False

def maxProduct(words):
    """
    :type words: List[str]
    :rtype: int
    """
    max_length = 0
    
    if len(words) < 2:
        return 0
    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if not self.shareCommonLetter(words[i], words[j]):
                max_length = max(max_length, len(words[i]) * len(words[j]))
    return max_length

def kPair(nums1, nums2):
    res = []
    for n in nums1:
        for m in nums2:
            if len(res) > 0 and n + m < sum(res[-1]):
                top = res.pop()
                res.append([n, m])
                res.append(top)
            else:
                res.append([n, m])
    return res