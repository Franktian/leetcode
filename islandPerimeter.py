def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res += self.getPerimeter(grid, i, j)
    return res
    
def getPerimeter(self, grid, i, j):
    adj = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
    res = 0
    
    for x, y in adj:
        if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
            res += 1
    return res


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    valid = True
    if len(s) < 3:
        return True
    
    for i in range(len(s)):
        sub = s[:i] + s[i + 1:]
        print sub
        
        if isPalindrome(sub):
            return True

    return False

def isPalindrome(s):
    for i in range(len(s) / 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
