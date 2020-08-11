class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return []
        
        rows, cols = len(board), len(board[0])

        # 最外面四边的'O'肯定不用改，先把这四条边的'O'找到并放到一个list里。
        noChangeNeed = []
        for i in [0, rows-1]:
            for j in range(cols):
                if board[i][j] == 'O': noChangeNeed.append([i,j])
        for j in [0, cols-1]:
            for i in range(rows):
                if board[i][j] == 'O': noChangeNeed.append([i,j])

        def is_legal_coordinate(coor):
            if coor[0] < 0 or coor[0] > rows - 1: return False
            if coor[1] < 0 or coor[1] > cols - 1: return False
            return True
        
        visited = []
        def from_nochange_node_bfs(coord):
            x, y = coord[0], coord[1]
            if [x,y] in visited:
                return
            visited.append([x,y])
            for coor in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                if is_legal_coordinate(coor) and board[coor[0]][coor[1]] == 'O' and coor not in visited:
                    noChangeNeed.append(coor)
                    from_nochange_node_bfs(coor)
            return
        
        # 从最外面四条边那些肯定不变的'O'出发，逐步找到所有不需要变化的'O'。
        for coor in noChangeNeed:
            from_nochange_node_bfs(coor)
        # 然后遍历整个二维数组把需要替换成'X'给替换了。    
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if board[i][j] == 'O' and [i,j] not in noChangeNeed:
                    board[i][j] = 'X'
        return
        
"""
https://leetcode-cn.com/submissions/detail/97125631/

59 / 59 个通过测试用例
状态：通过
执行用时：1092 ms
内存消耗：18.2 MB
"""
"""
执行用时：1092 ms, 在所有 Python 提交中击败了5.13%的用户
内存消耗：18.2 MB, 在所有 Python 提交中击败了13.46%的用户
"""
