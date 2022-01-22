class Solution:
    def removePalindromeSub(self, s: str) -> int:

        def is_palindrome_v2(s):
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-1-i]:
                    return False
            return True
        
        return 1 if is_palindrome_v2(s) else 2
        
"""
https://leetcode-cn.com/submissions/detail/261284566/

执行用时：32 ms, 在所有 Python3 提交中击败了65.50%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了42.69%的用户
通过测试用例：
48 / 48
"""
