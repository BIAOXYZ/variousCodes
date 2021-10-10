class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        
        oneDimensionArr = [i for arr in grid for i in arr]
        if len(set(oneDimensionArr)) == 1:
            return 0
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != 0:
                    return -1
        
        oneDimensionArr.sort()
        if m % 2 == 1 and n % 2 == 1:
            targetIndexes = [(m * n) / 2]
        else:
            targetIndexes = [(m * n) / 2 - 1, (m * n) / 2]
        
        res = float('inf')
        for ind in targetIndexes:
            tmp = 0
            for i in range(m*n):
                tmp += abs(oneDimensionArr[i] - oneDimensionArr[ind]) / x
            res = min(res, tmp)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/227344789/

19 / 42 个通过测试用例
状态：解答错误

输入：
[[931,128],[639,712]]
73
输出：
-1
预期：
12
"""
