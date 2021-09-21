class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 好久没有手动狗头题了。。。
        return len(s.split()[-1])
        
"""
https://leetcode-cn.com/submissions/detail/221628636/

58 / 58 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.2 MB

执行用时：16 ms, 在所有 Python 提交中击败了71.21%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了64.29%的用户
"""
