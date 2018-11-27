def hasPath(self, maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """
    queue = [start]
    m = len(maze)
    n = len(maze[0])
    dirs = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )

    while queue:
        i, j = queue.pop(0)
        maze[i][j] = 2

        if i == destination[0] and j == destination[1]:
            return True

        for x, y in dirs:
            row = i + x
            col = j + y
            while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                row += x
                col += y
            row -= x
            col -= y

            if maze[row][col] == 0:
                queue.append([row, col])

    return False
