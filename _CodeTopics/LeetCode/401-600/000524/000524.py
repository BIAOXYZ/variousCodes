class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """

        def is_subsequence(s1, s2):
            i = j = 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1; j += 1
                else:
                    i += 1
            if j == len(s2):
                return True
            return False
        
        res = ""
        for elem in dictionary:
            if is_subsequence(s, elem) and \
                (len(elem) > len(res) or (len(elem) == len(res) and elem < res)):
                res = elem
        return res
        
"""
https://leetcode-cn.com/submissions/detail/218933489/

31 / 31 个通过测试用例
状态：通过
执行用时: 376 ms
内存消耗: 15.9 MB

执行用时：376 ms, 在所有 Python 提交中击败了49.31%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了13.89%的用户
"""
