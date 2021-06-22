class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 手动狗头题
        # 另外其实不做切片也没问题，因为二进制开头两位是 0b，不会影响 1 的个数。
        return str(bin(n))[2:].count('1')
        
"""
https://leetcode-cn.com/submissions/detail/188946670/

601 / 601 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.1 MB

执行用时：12 ms, 在所有 Python 提交中击败了95.18%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了15.12%的用户
"""
