class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        directions = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        def is_legal_coor(coor):
            x, y = coor
            return 0 <= x < n and 0 <= y < n
        
        remainOnBoardPaths = 0
        def backtrack(coor, step):
            # 这种写法就属于，不管三七二十一都往下继续走回溯，但是
            ## 到了下一层开头的地方再判断合法性，不合法就直接返回。
            # 还有另一种模式是在下面的for循环处就判断好合法性，保证
            ## 进入下一层的坐标一定都是合法的。
            if not is_legal_coor(coor):
                return
            if step == k:
                nonlocal remainOnBoardPaths
                remainOnBoardPaths += 1
                return
            for d in directions:
                backtrack((coor[0]+d[0], coor[1]+d[1]), step+1)
        
        if k == 0 and is_legal_coor((row, column)):
            return 1.0
        backtrack((row, column), 0)
        return remainOnBoardPaths / 8**k
        
"""
https://leetcode-cn.com/submissions/detail/269280674/

11 / 22 个通过测试用例
状态：超出时间限制

最后执行的输入：
8
30
6
4
"""
