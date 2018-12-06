class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        move = 1 if player == 1 else -1

        self.rows[row] += move
        self.cols[col] += move

        if row == col:
            self.diag += move

        if row + col == self.n - 1:
            self.anti_diag += move

        if self.rows[row] == self.n or self.cols[col] == self.n or self.diag == self.n or self.anti_diag == self.n:
            return 1

        if self.rows[row] == -self.n or self.cols[col] == -self.n or self.diag == -self.n or self.anti_diag == -self.n:
            return 2

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)