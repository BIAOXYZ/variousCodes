class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        def str_to_dict(s):
            dic = {}
            for ch in s:
                if ch in dic:
                    dic[ch] += 1
                else:
                    dic[ch] = 1
            return dic
        
        dic = str_to_dict(s)
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/133018753/

104 / 104 个通过测试用例
状态：通过
执行用时: 108 ms
内存消耗: 13.8 MB

执行用时：108 ms, 在所有 Python 提交中击败了79.54%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了21.14%的用户
"""
