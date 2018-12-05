class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nums = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    nums += 1
                    self.dfs(grid, i, j)

        return nums

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '#'

        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    queue = [(i, j)]
                    while queue:
                        x, y = queue.pop(0)

                        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == '1':
                            grid[x][y] = '#'
                            queue.append((x + 1, y))
                            queue.append((x - 1, y))
                            queue.append((x, y + 1))
                            queue.append((x, y - 1))
        return res
