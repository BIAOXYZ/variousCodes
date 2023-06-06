class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # 求矩阵的所有列的时候用到了一个技巧 `zip(*grid)`
        # 此外，解包后里面的元素（也就是矩阵的列）已经是 tuple 类型了，比如：
        # grid = [[3,2,1],[1,7,6],[2,7,7]]
        # list(zip(*grid)) = [(3, 1, 2), (2, 7, 7), (1, 6, 7)]
        cols = list(zip(*grid))
        ## print(cols)
        rows = [tuple(row) for row in grid]
        ## print(rows)

        row_ctr, col_ctr = Counter(rows), Counter(cols)
        res = 0
        for k, v in row_ctr.items():
            if k in col_ctr:
                res += v * col_ctr[k]
        return res
        
"""
https://leetcode.cn/submissions/detail/438014395/

执行用时：
60 ms
, 在所有 Python3 提交中击败了
86.10%
的用户
内存消耗：
20.6 MB
, 在所有 Python3 提交中击败了
29.76%
的用户
通过测试用例：
72 / 72
"""
