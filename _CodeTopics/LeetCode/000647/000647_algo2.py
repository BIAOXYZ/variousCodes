class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        length = len(s)
        res = 0
        for i in range(length):
            left = right = i
            while left >= 0 and right <= length - 1:
                if s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break
            if i < length - 1 and s[i+1] == s[i]:
                left, right = i, i + 1
                while left >= 0 and right <= length - 1:
                    if s[left] == s[right]:
                        res += 1
                        left -= 1
                        right += 1
                    else:
                        break  
        return res
        
"""
https://leetcode-cn.com/submissions/detail/99824187/

130 / 130 个通过测试用例
状态：通过
执行用时：84 ms
内存消耗：12.8 MB
"""
"""
执行用时：84 ms, 在所有 Python 提交中击败了76.21%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了66.94%的用户
"""
