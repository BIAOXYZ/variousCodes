class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        x0, y0, x1, y1 = coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]
        for x, y in coordinates[2:]:
            if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/138921631/

79 / 79 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.5 MB

执行用时：36 ms, 在所有 Python 提交中击败了34.43%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了32.79%的用户
"""
