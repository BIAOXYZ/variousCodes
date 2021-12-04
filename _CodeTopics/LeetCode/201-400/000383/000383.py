class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        def str_to_alphabeta_list(s):
            res = [0 for _ in range(26)]
            for ch in s:
                res[ord(ch)-ord('a')] += 1
            return res
        
        listR, listM = str_to_alphabeta_list(ransomNote), str_to_alphabeta_list(magazine)
        return all(listR[i] <= listM[i] for i in range(26))
        
"""
https://leetcode-cn.com/submissions/detail/245135100/

执行用时：52 ms, 在所有 Python 提交中击败了64.29%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了68.24%的用户
通过测试用例：
126 / 126
"""
