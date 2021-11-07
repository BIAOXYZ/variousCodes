class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        res = 0
        start = end = 0
        for i in range(n):
            if word[i] in vowels:
                if i == 0 or i == n - 1:
                    res += n
                else:
                    # 对于元音字母在中间位置的情况，包括三部分：原音字母本身；纯左边和纯右边；既有左边也有右边。
                    res += 1
                    res += i + n-i-1 
                    res += i * (n-i-1)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/236251887/

51 / 51 个通过测试用例
状态：通过
执行用时: 116 ms
内存消耗: 17.1 MB
"""
