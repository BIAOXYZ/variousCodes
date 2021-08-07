class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        
        # up
        if rMove >= 2:
            row = rMove - 1
            while row >= 0 and board[row][cMove] != color and board[row][cMove] != ".":
                row -= 1
            if row != -1 and row != rMove - 1 and board[row][cMove] == color: return True
        
        # down
        if rMove <= 5:
            row = rMove + 1
            while row <= 7 and board[row][cMove] != color and board[row][cMove] != ".":
                row += 1
            if row != 8 and row != rMove + 1 and board[row][cMove] == color: return True
        
        # left
        if cMove >= 2:
            col = cMove - 1
            while col >= 0 and board[cMove][col] != color and board[cMove][col] != ".":
                col -= 1
            if col != -1 and col != cMove - 1 and board[cMove][col] == color: return True      
        
        # right
        if cMove <= 5:
            col = cMove + 1
            while col <= 7 and board[cMove][col] != color and board[cMove][col] != ".":
                col += 1
            if col != 8 and col != cMove + 1 and board[cMove][col] == color: return True
        
        # up-right
        row, col = rMove - 1, cMove + 1
        while row >= 0 and col <= 7 and board[row][col] != color and board[row][col] != ".":
            row -= 1; col += 1
        if row != -1 and col != 8 and row != rMove - 1 and col != cMove + 1 and board[row][col] == color: return True
        
        # up-left
        row, col = rMove - 1, cMove - 1
        while row >= 0 and col >= 0 and board[row][col] != color and board[row][col] != ".":
            row -= 1; col -= 1
        if row != -1 and col != -1 and row != rMove - 1 and col != cMove - 1 and board[row][col] == color: return True
        
        # down-left
        row, col = rMove + 1, cMove - 1
        while row <= 7 and col >= 0 and board[row][col] != color and board[row][col] != ".":
            row += 1; col -= 1
        if row != 8 and col != -1 and row != rMove + 1 and col != cMove - 1 and board[row][col] == color: return True
        
        # down-right
        row, col = rMove + 1, cMove + 1
        while row <= 7 and col <= 7 and board[row][col] != color and board[row][col] != ".":
            row += 1; col += 1
        if row != 8 and col != 8 and row != rMove + 1 and col != cMove + 1 and board[row][col] == color: return True
        
        return False
    
"""
https://leetcode-cn.com/submissions/detail/204409783/

174 / 213 个通过测试用例
状态：解答错误

最后执行的输入：
[["W","W",".","W","B","B",".","."],["B",".","W",".","B","B","B","."],["B","B","W",".","W","W","W","B"],[".",".","W","B","B",".","B","B"],["W",".","W","B","W","W","W","W"],["B","W","W","B","B","B","B","."],["W","B","B","W",".","W",".","B"],["W","W","B","W",".",".",".","B"]]
6
4
"B"
输出：
false
预期：
true
"""
