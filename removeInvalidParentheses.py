class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
    
        l = 0
        r = 0

        for c in s:
            if c == '(':
                l += 1
            if c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        self.dfs(s, 0, l, r, res)

        return res
    
    def dfs(self, s, start, l, r, res):
        if l == 0 and r == 0 and self.isValid(s):
            res.append(s)
            return

        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue

            sub = s[:i] + s[i + 1:]
            if s[i] == '(' and l > 0:
                self.dfs(sub, i, l - 1, r, res)

            if s[i] == ')' and r > 0:
                self.dfs(sub, i, l, r - 1, res)

    def isValid(self, s):
        # O(n)
        count = 0
        
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1

            if count < 0:
                return False
        return count == 0
