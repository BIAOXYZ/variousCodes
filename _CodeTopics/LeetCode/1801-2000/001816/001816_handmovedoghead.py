class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # 手动狗头题
        return ' '.join(s.split()[:k])
        
"""
https://leetcode-cn.com/submissions/detail/245622098/

执行用时：16 ms, 在所有 Python 提交中击败了75.56%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了33.33%的用户
通过测试用例：
72 / 72
"""
