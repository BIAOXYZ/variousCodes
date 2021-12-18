class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        res = 0
        visited = set()
        rows, cols = len(board), len(board[0])
        directions = [[1,0],[0,1]]

        def is_legal(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def dfs(x, y):
            # 从下面 for 循环来看，这个 if 判断是没用的，不过无所谓，留着吧。
            if (x, y) in visited:
                return
            visited.add((x, y))
            for d in directions:
                nextX, nextY = x + d[0], y + d[1]
                if is_legal(nextX, nextY) and board[nextX][nextY] == 'X':
                    dfs(nextX, nextY)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                else:
                    if (i, j) not in visited:
                        res += 1
                        dfs(i, j)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/249742335/

执行用时：32 ms, 在所有 Python 提交中击败了21.62%的用户
内存消耗：16.1 MB, 在所有 Python 提交中击败了5.41%的用户
通过测试用例：
27 / 27
"""
