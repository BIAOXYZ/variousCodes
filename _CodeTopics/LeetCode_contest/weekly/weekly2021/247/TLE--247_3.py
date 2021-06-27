class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        n = len(word)
        res = n
        
        for i in range(n-1):
            dic = {word[i]:1}
            num_of_odd = 1
            for j in range(i+1, n):
                if word[j] not in dic or dic[word[j]] % 2 == 0:
                    num_of_odd += 1
                else:
                    num_of_odd -= 1
                if num_of_odd <= 1:
                    res += 1
                dic[word[j]] = dic.setdefault(word[j], 0) + 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/190086997/

57 / 88 个通过测试用例
状态：超出时间限制
"""
