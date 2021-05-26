class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # Brian Kernighan 算法。
        # 其实更准确说是一个trick，之前在 LC338 和 LC1178 见过，只是当时官方答案直接用了，并没有说明出处。

        res = 0
        tmp = x ^ y
        while tmp:
            tmp &= tmp - 1
            res += 1
        return res

"""
https://leetcode-cn.com/submissions/detail/181184272/

149 / 149 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了83.46%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了28.23%的用户
"""
