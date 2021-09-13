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
            if is_subsequence(s, elem) and (len(elem) > len(res) or elem < res):
                res = elem
        return res
        
"""
https://leetcode-cn.com/submissions/detail/218931658/

20 / 31 个通过测试用例
状态：解答错误

最后执行的输入：
"aaa"
["aaa","aa","a"]
输出：
"a"
预期结果：
"aaa"
"""
