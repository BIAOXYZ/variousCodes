from collections import deque
class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        
        # 这里最好先处理旋转。
        def stone_fall(lis, n):
            stk = deque([])
            for i in range(n-1, -1, -1):
                if lis[i] == ".":
                    stk.append(i)
                elif lis[i] == "*":
                    stk.clear()
                elif lis[i] == "#":
                    if stk:
                        j = stk.popleft()
                        lis[i], lis[j] = lis[j], lis[i]
        
        rownum, colnum = len(box), len(box[0])
        for row in box:
            stone_fall(row, colnum)
        
        res = [[0 for _ in range(rownum)] for _ in range(colnum)]
        for i in range(colnum):
            for j in range(rownum):
                # 注意是90旋转，不是转置！
                res[i][j] = box[rownum-1-j][i]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/177822686/

36 / 87 个通过测试用例
状态：解答错误

最后执行的输入：
[["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
"""
