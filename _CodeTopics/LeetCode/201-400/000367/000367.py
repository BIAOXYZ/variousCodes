class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        i = 1
        while i**2 < num:
            i += 1
        return i**2 == num
        
"""
https://leetcode-cn.com/submissions/detail/235221725/

执行用时：20 ms, 在所有 Python 提交中击败了36.52%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了36.27%的用户
通过测试用例：
70 / 70
"""
