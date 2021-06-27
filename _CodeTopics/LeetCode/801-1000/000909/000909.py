class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def num_to_coordinate(num):
            if num % n != 0:
                row = n - 1 - num / n
                # 从左到右
                if (num / n) & 1 == 0:
                    col = num % n - 1
                # 从右到左
                else:
                    col = n - num % n
            else:
                row = n - 1 - (num / n - 1)
                if (num / n) & 1 == 0:
                    col = 0
                else:
                    col = n - 1
            return row, col

        n = len(board)
        stk = [1]
        step = 0
        visited = set()

        while stk:
            nextLevel = []
            for elem in stk:
                if elem not in visited:
                    visited.add(elem)
                else:
                    continue
                for i in range(1, 7):
                    nextElem = elem + i
                    if nextElem == n * n:
                        return step + 1
                    elif nextElem < n * n:
                        row, col = num_to_coordinate(nextElem)
                        if board[row][col] != -1:
                            if board[row][col] != n * n:
                                nextLevel.append(board[row][col])
                            else:
                                return step + 1
                        else:
                            nextLevel.append(nextElem)                  
            step += 1
            stk = nextLevel[:]
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/190122037/

211 / 211 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 13.1 MB

执行用时：72 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了20.00%的用户
"""
