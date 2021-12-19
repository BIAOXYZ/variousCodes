class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for w in words:
            if is_palindrome(w):
                return w
        return ''
    
"""
https://leetcode-cn.com/submissions/detail/249835204/

266 / 266 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 13.2 MB
"""
