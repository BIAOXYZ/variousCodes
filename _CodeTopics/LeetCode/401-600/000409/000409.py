class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        def str_to_dic(s):
            dic = {}
            for ch in s:
                dic[ch] = dic.setdefault(ch, 0) + 1
            return dic
        
        dic = str_to_dic(s)
        res = 0
        flag = False
        for v in dic.values():
            if v % 2 == 0:
                res += v
            else:
                flag = True
                res += v-1
        return res if not flag else res + 1
          
"""
https://leetcode-cn.com/submissions/detail/160653939/

95 / 95 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.9 MB

执行用时：12 ms, 在所有 Python 提交中击败了98.53%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了83.46%的用户
"""
