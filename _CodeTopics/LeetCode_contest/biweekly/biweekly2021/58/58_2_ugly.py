class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        
        def is_legal(x, y):
            if x < 0 or x > 7: return False
            if y < 0 or y > 7: return False
            return True
        
        # up
        row, col = rMove - 1, cMove
        row2, col2 = row, col
        while is_legal(row, col) and board[row][col] != color and board[row][col] != ".":
            row -= 1
        if is_legal(row, col) and (row != row2 or col != col2) and board[row][col] == color: return True
        
        # down
        row, col = rMove + 1, cMove
        row2, col2 = row, col
        while is_legal(row, col) and board[row][col] != color and board[row][col] != ".":
            row += 1
        if is_legal(row, col) and (row != row2 or col != col2) and board[row][col] == color: return True
        
        # left
        row, col = rMove, cMove - 1
        row2, col2 = row, col
        while is_legal(row, col) and board[row][col] != color and board[row][col] != ".":
            col -= 1
        if is_legal(row, col) and (row != row2 or col != col2) and board[row][col] == color: return True    
        
        # right
        row, col = rMove, cMove + 1
        row2, col2 = row, col
        while is_legal(row, col) and board[row][col] != color and board[row][col] != ".":
            col += 1
        if is_legal(row, col) and (row != row2 or col != col2) and board[row][col] == color: return True         
        
        # up-right
        row, col = rMove - 1, cMove + 1
        row2, col2 = row, col
        while is_legal(row, col) and board[row][col] != color and board[row][col] != ".":
            row -= 1; col += 1
        if is_legal(row, col) and (row != row2 or col != col2) and board[row][col] == color: return True 
        
        # up-left
        row, col = rMove - 1, cMove - 1
        row2, col2 = row, col
        while is_legal(row, col) and board[row][col] != color and board[row][col] != ".":
            row -= 1; col -= 1
        if is_legal(row, col) and (row != row2 or col != col2) and board[row][col] == color: return True 
        
        # down-left
        row, col = rMove + 1, cMove - 1
        row2, col2 = row, col
        while is_legal(row, col) and board[row][col] != color and board[row][col] != ".":
            row += 1; col -= 1
        if is_legal(row, col) and (row != row2 or col != col2) and board[row][col] == color: return True 
        
        # down-right
        row, col = rMove + 1, cMove + 1
        row2, col2 = row, col
        while is_legal(row, col) and board[row][col] != color and board[row][col] != ".":
            row += 1; col += 1
        if is_legal(row, col) and (row != row2 or col != col2) and board[row][col] == color: return True 
        
        return False
    
"""
https://leetcode-cn.com/submissions/detail/204415137/

213 / 213 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13.3 MB
"""
