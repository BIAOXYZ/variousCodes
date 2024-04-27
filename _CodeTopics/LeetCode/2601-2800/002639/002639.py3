from functools import reduce
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        # 求矩阵的所有列的时候用到了一个技巧 `zip(*grid)`
        # 此外，解包后里面的元素（也就是矩阵的列）已经是 tuple 类型了，比如：
        # grid = [[4,3,2,1],[44,33,22,11],[444,333,222,111]]
        # cols_list = list(zip(*grid)) 
        # print(cols_list)  # [(4, 44, 444), (3, 33, 333), (2, 22, 222), (1, 11, 111)]

        col_num = len(grid[0])
        cols_list = list(zip(*grid))
        res = [-1] * col_num

        func_len_str = lambda x : len(str(x))
        for i in range(col_num):
            res[i] = reduce(max, list(map(func_len_str, cols_list[i])))
        return res
        
"""
https://leetcode.cn/problems/find-the-width-of-columns-of-a-grid/submissions/527602954?envType=daily-question&envId=2024-04-27

通过
提交于 2024.04.27 18:52

执行用时分布
57
ms
击败
10.40%
使用 Python3 的用户
消耗内存分布
18.18
MB
击败
5.60%
使用 Python3 的用户
"""
