class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 还是手动狗头，和上一个比只是加个中括号，我目前还没想出来这俩有啥区别。。。上一个是这样：
        # return sum(1 for i in range(32) if n & (1 << i))
        return sum([1 for i in range(32) if n & (1 << i)])
        
"""
https://leetcode-cn.com/submissions/detail/158119386/

601 / 601 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13 MB

执行用时：8 ms, 在所有 Python 提交中击败了98.99%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了40.24%的用户
"""
