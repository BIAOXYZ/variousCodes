class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        # 这题要是还有被 0 完全包围的物品就哭了。。。
        
        m, n = len(grid), len(grid[0])
        lis = []
        for i in range(m):
            for j in range(n):
                if pricing[0] <= grid[i][j] <= pricing[1]:
                    lis.append([i,j])
        ##print lis
        def cmp_func(coor1, coor2):
            x1, y1 = coor1[0], coor1[1]
            x2, y2 = coor2[0], coor2[1]
            dis1 = abs(x1 - start[0]) + abs(y1 - start[1])
            dis2 = abs(x2 - start[0]) + abs(y2 - start[1])
            if dis1 < dis2 or grid[x1][y1] < grid[x2][y2] or x1 < x2 or y1 < y2:
                return -1
            return 1
        
        lis.sort(key=cmp_func)
        return lis[:k]
"""
https://leetcode-cn.com/submissions/detail/261390005/

0 / 49 个通过测试用例
状态：执行出错

执行出错信息：
TypeError: cmp_func() takes exactly 2 arguments (1 given)
    lis.sort(key=cmp_func)
Line 29 in highestRankedKItems (Solution.py)
    ret = Solution().highestRankedKItems(param_1, param_2, param_3, param_4)
Line 66 in _driver (Solution.py)
    _driver()
Line 76 in <module> (Solution.py)
最后执行的输入：
[[1,2,0,1],[1,3,0,1],[0,2,5,1]]
[2,5]
[0,0]
3
"""
