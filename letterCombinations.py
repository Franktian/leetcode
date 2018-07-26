def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    mappings = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    
    if len(digits) == 0:
        return []

    res = [""]
    
    for d in digits:
        lst = mappings[d]
        temp = []
        
        for c in lst:
            for s in res:
                temp.append(s + c)
        res = temp
    return res
