class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        def can_catch_pawn(x, y, direction):
            if direction == 0:
                for i in range(x-1, -1, -1):
                    if board[i][y] == 'p': return 1
                    elif board[i][y] == 'B': return 0
            elif direction == 1:
                for i in range(x+1, len(board)):
                    if board[i][y] == 'p': return 1
                    elif board[i][y] == 'B': return 0
            elif direction == 2:
                for j in range(y-1, -1, -1):
                    if board[x][j] == 'p': return 1
                    elif board[x][j] == 'B': return 0
            else:
                for j in range(y+1, len(board[0])):
                    if board[x][j] == 'p': return 1
                    elif board[x][j] == 'B': return 0
            return 0

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'R':
                    return sum([can_catch_pawn(i, j, d) for d in range(4)])
        
"""
https://leetcode-cn.com/submissions/detail/201809318/

24 / 24 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13 MB

执行用时：8 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了58.33%的用户
"""
