class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def is_palindrome(s):
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def left_part_and_right_part_can_form_palindrome(lstr, rstr):
            n = len(lstr)
            left, right = 0, n - 1
            while left < right:
                if lstr[left] == rstr[right]:
                    left += 1
                    right -= 1
                else:
                    break
            if left >= right:
                return True
            else:
                return is_palindrome(lstr[left:right+1]) or is_palindrome(rstr[left:right+1])
        
        return left_part_and_right_part_can_form_palindrome(a, b) or left_part_and_right_part_can_form_palindrome(b, a)
        
"""
https://leetcode.cn/submissions/detail/414801972/

执行用时：
156 ms
, 在所有 Python3 提交中击败了
8.47%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
93.22%
的用户
通过测试用例：
109 / 109
"""
