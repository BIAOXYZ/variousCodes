class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # 等价于两个数异或后得到的结果中1的个数。

        res = 0
        tmp = x ^ y
        while tmp:
            if tmp % 2 != 0:
                res += 1
                tmp = (tmp - 1) / 2
            else:
                tmp /= 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/181182759/

149 / 149 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.3 MB

执行用时：24 ms, 在所有 Python 提交中击败了28.48%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.35%的用户
"""
