class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        if not s:
            return [[]]
        res = []
        for i in range(1, len(s)+1):
            currStr = s[:i]
            if is_palindrome(currStr):
                for lis in self.partition(s[i:]):
                    res.append([currStr] + lis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/151945731/

32 / 32 个通过测试用例
状态：通过
执行用时: 276 ms
内存消耗: 44.1 MB

执行用时：276 ms, 在所有 Python 提交中击败了11.76%的用户
内存消耗：44.1 MB, 在所有 Python 提交中击败了78.82%的用户
"""
