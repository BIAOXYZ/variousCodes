class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 官方答案的做法：利用 LC231 的办法先判断是 2 的幂；然后判断这个唯一的1出现在“第偶数个二进制位上”。
        # mask 的二进制表示 (10101010101010101010101010101010)_2​ 其对应的16进制为 0xaaaaaaaa。
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0
        
"""
https://leetcode-cn.com/submissions/detail/182354233/

1061 / 1061 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB

执行用时：20 ms, 在所有 Python 提交中击败了87.95%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了35.54%的用户
"""
