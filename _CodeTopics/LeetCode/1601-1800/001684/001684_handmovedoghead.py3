class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        # 手动狗头题
        return sum(1 for word in words if all(ch in allowed for ch in word))
        
"""
https://leetcode.cn/submissions/detail/380214914/

执行用时：
100 ms
, 在所有 Python 提交中击败了
61.90%
的用户
内存消耗：
14.8 MB
, 在所有 Python 提交中击败了
35.71%
的用户
通过测试用例：
74 / 74
"""
