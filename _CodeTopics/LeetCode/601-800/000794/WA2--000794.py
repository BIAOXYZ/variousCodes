class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """

        totalX = totalO = 0
        for s in board:
            for ch in s:
                if ch == 'X':
                    totalX += 1
                elif ch == 'O':
                    totalO += 1
        if totalO > totalX or totalX - totalO >= 2:
            return False
        
        def check_row(ch):
            num = 0
            for row in board:
                if all(row[i] == ch for i in range(3)):
                    num += 1
            return num
        def check_col(ch):
            num = 0
            for i in range(3):
                if all(board[j][i] == ch for j in range(3)):
                    num += 1
            return num
        def check_diagonal(ch):
            num = 0
            if all(board[i][i] == ch for i in range(3)):
                num += 1
            if all(board[i][2-i] == ch for i in range(3)):
                num += 1
            return num
        
        totalTripleX = totalTripleO = 0
        totalTriplesX = check_row('X') + check_col('X') + check_diagonal('X')
        totalTriplesO = check_row('O') + check_col('O') + check_diagonal('O')
        if totalTriplesX != 0 and totalTriplesO != 0:
            return False
        totalTriples = totalTriplesX + totalTriplesO
        if totalTriples > 2:
            return False
        if totalTriples == 2 and any(board[i][j] == '.' for i in range(3) for j in range(3)):
            return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/246678655/

105 / 109 个通过测试用例
状态：解答错误

输入：
["XXX","XOO","OO "]
输出：
true
预期结果：
false
"""
