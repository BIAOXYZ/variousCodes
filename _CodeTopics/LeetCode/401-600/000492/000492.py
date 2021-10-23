class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        res = [area, 1]
        i = 1
        while i**2 <= area:
            if area % i == 0:
                res[0] = area / i
                res[1] = i
            i += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/231576464/

执行用时：16 ms, 在所有 Python 提交中击败了90.16%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了93.44%的用户
通过测试用例：52 / 52
"""
"""
# 2021.10.23
# 从本题开始，用新的复制格式。
"""
