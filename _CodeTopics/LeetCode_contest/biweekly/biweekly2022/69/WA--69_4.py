class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """
        
        # 核心就是检查以每个 0 的格子为左上角，邮票大小区域内是否有1。
        # 但是就这么trivial的去遍历肯定会超时。
        
        m, n = len(grid), len(grid[0])
        minh, minw = m, n
        cols = [[grid[i][j] for i in range(m)] for j in range(n)]
        rows = [grid[i] for i in range(m)]
        for elem in cols:
            elem.append(1)
        for elem in rows:
            elem.append(1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                h = cols[j].index(1, i)
                w = rows[i].index(1, j)
                if h < m:
                    minh = min(minh, h - i)
                if w < n:
                    minw = min(minw, w - j)
            if minh < stampHeight or minw < stampWidth:
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/256412944/

40 / 56 个通过测试用例
状态：解答错误

输入：
[[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
9
4
输出：
false
预期：
true
"""
