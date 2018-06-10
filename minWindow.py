from collections import defaultdict
import sys

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    count = len(t)
    min_size = len(s) + 1
    left = min_left = 0
    counts = {}

    for c in t:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    
    for right in range(len(s)):        
        if s[right] in counts:
            counts[s[right]] -= 1
            if counts[s[right]] >= 0:
                count -= 1
            
            if count == 0:
                while True:
                    if s[left] in counts:
                        if counts[s[left]] < 0:
                            counts[s[left]] += 1
                        else:
                            break
                    left += 1
                
                if right - left + 1 < min_size:
                    min_left = left
                    min_size = right - left + 1
        
    if min_size < len(s) + 1:
        return s[min_left:min_left + min_size]
    else:
        return ''