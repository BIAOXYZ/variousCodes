class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 手动狗头，官方答案改变了下
        return sum(1 for i in range(32) if n & (1 << i))
        
"""
https://leetcode-cn.com/submissions/detail/158118976/

601 / 601 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 12.8 MB

执行用时：8 ms, 在所有 Python 提交中击败了98.99%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了92.35%的用户
"""
