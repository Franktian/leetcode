def shortestPalindrome(s):
    rev = s[::-1]
    
    for i in range(len(s)):
        if s.startswith(rev[i:]):
            return rev[:i] + s