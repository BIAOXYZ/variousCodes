class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def isValidSudokuForList(l):
            dic = dict()
            for elem in l:
                if elem == '.':
                    continue
                elif dic.has_key(elem):
                    return False
                else:
                    dic[elem] = 1
            return True
        
        def formList(l1,l2):
            a, b = l1[0], l1[1]
            x, y = l2[0], l2[1]
            if a == x:
                return [board[x][i] for i in range(9)]
            elif b == y:
                return [board[i][b] for i in range(9)]
            else:
                resList = []
                for i in range(a,a+3):
                    for j in range(b,b+3):
                        resList.append(board[i][j])
                return resList
        
        diagonal = [
            [[0,0],[2,2]],[[0,3],[2,5]],[[0,6],[2,8]],
            [[3,0],[5,2]],[[3,3],[5,5]],[[3,6],[5,8]],
            [[6,0],[8,2]],[[6,3],[8,5]],[[6,6],[8,8]]
        ]
        for coordinate in diagonal:
            if not isValidSudokuForList(formList(coordinate[0],coordinate[1])):
                return False
        
        start, end = 0, 8
        for i in range(9):
            if not isValidSudokuForList(formList([i,start],[i,end])):
                return False
            if not isValidSudokuForList(formList([start,i],[end,i])):
                return False
        return True

"""
https://leetcode-cn.com/submissions/detail/80617922/

504 / 504 个通过测试用例
状态：通过
执行用时：48 ms
内存消耗：12.7 MB
"""
"""
上一个 WA--000036.py 之所以不对是因为第43行range里应该是9，低级失误。只要改了这个数字就过了。
"""
