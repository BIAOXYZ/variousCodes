class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        n = len(word)
        
        for i in range(n-4):
            for j in range(i+4, n):
                if set(word[i:j+1]) == vowels:
                    res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/236234334/

88 / 88 个通过测试用例
状态：通过
执行用时: 212 ms
内存消耗: 13.1 MB
"""
