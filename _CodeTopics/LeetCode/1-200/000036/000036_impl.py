class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def check_row(i):
            se = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in se:
                    return False
                else:
                    se.add(board[i][j])
            return True
        def check_column(j):
            se = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in se:
                    return False
                else:
                    se.add(board[i][j])
            return True
        def check_square(x,y):
            se = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in se:
                        return False
                    else:
                        se.add(board[i][j])
            return True
        
        for i in range(9):
            if not check_row(i) or not check_column(i):
                return False
        upLeftCoors = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for x, y in upLeftCoors:
            if not check_square(x, y):
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/220208482/

507 / 507 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.1 MB

执行用时：36 ms, 在所有 Python 提交中击败了52.44%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了62.09%的用户
"""
