class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        # 手动狗头题
        return hex(num)[2:] if num >= 0 else hex(0xffffffff + num + 1)[2:]
        
"""
https://leetcode-cn.com/submissions/detail/225055334/

100 / 100 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.8 MB

执行用时：12 ms, 在所有 Python 提交中击败了92.19%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了95.31%的用户
"""
