class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        length = len(word)
        rows, cols = len(board), len(board[0])
        
        def is_legal_coordinate(x, y):
            if x < 0 or x > rows - 1: return False
            if y < 0 or y > cols - 1: return False
            return True
        
        def backtrace_from(coor, currArr, pos):
            # 如果某个点坐标已经在currArr里了，那么当然不能再用了，也就是这条路径肯定是挂了。
            # 比如例子里输入为"ABCB"时。
            if coor in currArr:
                return False
            # 这个就不用说了。
            x, y = coor[0], coor[1]
            if not is_legal_coordinate(x,y) or board[x][y] != word[pos]:
                return False
            # 假设pos为0，过了上面那个判定后，尽管pos还是0，但是实际上第一个字母已经好了。
            # 所以程序运行到此处时，如果pos已经是length-1，那么已经有length个字母好了，可以返回True了。
            if pos == length - 1:
                return True

            ###currArr.append(coor)
            neighbors = [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
            res = False
            for nextCoor in neighbors:
                currArr.append(coor)
                res = res or backtrace_from(nextCoor, currArr, pos+1)
                currArr.pop()
            return res
        
        for i in range(rows):
            for j in range(cols):
                if backtrace_from([i,j], [], 0):
                    return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/107576697/

89 / 89 个通过测试用例
状态：通过
执行用时: 388 ms
内存消耗: 15.5 MB
"""
"""
执行用时：388 ms, 在所有 Python 提交中击败了9.71%的用户
内存消耗：15.5 MB, 在所有 Python 提交中击败了63.65%的用户
"""
