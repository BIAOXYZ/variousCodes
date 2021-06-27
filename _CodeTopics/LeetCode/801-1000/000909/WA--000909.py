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
                    if elem + i == n * n:
                        return step + 1
                    elif elem + i < n * n:
                        row, col = num_to_coordinate(elem + i)
                        if board[row][col] != -1:
                            nextLevel.append(board[row][col])
                        else:
                            nextLevel.append(elem + i)
            step += 1
            stk = nextLevel[:]
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/190114200/

183 / 211 个通过测试用例
状态：解答错误

最后执行的输入：
[[-1,-1,-1],[-1,9,8],[-1,8,9]]
输出：
2
预期结果：
1
"""
