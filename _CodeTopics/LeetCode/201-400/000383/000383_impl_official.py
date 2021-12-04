from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # 近似手动狗头
        return not Counter(ransomNote) - Counter(magazine)
        
"""
https://leetcode-cn.com/submissions/detail/245140331/

执行用时：72 ms, 在所有 Python 提交中击败了37.99%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了34.19%的用户
通过测试用例：
126 / 126
"""
