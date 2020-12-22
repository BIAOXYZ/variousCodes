import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        dic = collections.Counter(s)
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/133019041/

104 / 104 个通过测试用例
状态：通过
执行用时: 184 ms
内存消耗: 14.1 MB

执行用时：184 ms, 在所有 Python 提交中击败了51.01%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了11.00%的用户
"""
