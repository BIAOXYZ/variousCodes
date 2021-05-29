class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
        m, n = len(grid), len(grid[0])
        res = []
        
        # 先计算出最大的菱形的可能（能走几步）
        for row in range(m):
            for col in range(n):
                tmp = grid[row][col]
                hSteps = min(col-0, n-1-col)
                vSteps = (m-1-row)/2
                totalStep = min(hSteps, vSteps)
                if totalStep == 0:
                    res.append(tmp)
                    continue
                # 上一个错了在于只考虑了最大的菱形。
                for step in range(1, totalStep+1):
                    tmp += grid[row + step*2][col]
                    i = 1
                    while i < step:
                        tmp += grid[row+i][col-i] + grid[row+i][col+i]
                        tmp += grid[row + step*2 - i][col-i] + grid[row + step*2 - i][col+i]
                        i += 1
                    tmp += grid[row+step][col-step] + grid[row+step][col+step]
                    res.append(tmp)
                    tmp = grid[row][col]
        
        res = list(set(res))
        res.sort(reverse=True)
        return res[:3] if len(res) >= 3 else res
    
"""
https://leetcode-cn.com/submissions/detail/182032608/

112 / 112 个通过测试用例
状态：通过
执行用时: 788 ms
内存消耗: 14.4 MB
"""
