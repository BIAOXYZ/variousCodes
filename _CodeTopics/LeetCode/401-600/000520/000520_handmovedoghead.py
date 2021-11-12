class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        # 手动狗头题
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
        
"""
https://leetcode-cn.com/submissions/detail/238114692/

执行用时：20 ms, 在所有 Python 提交中击败了70.59%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了29.41%的用户
通过测试用例：
550 / 550
"""
