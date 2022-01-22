class Solution:
    def removePalindromeSub(self, s: str) -> int:

        # 我擦，被这道题给唬住了一小会还。。。想着双指针其实也没那么好处理啊，
        # 怎么这题就能只是个简单呢？后来一想，就 a 和 b 那不最多也就需要两次么？
        # 所以其实就是等价于判断整个字符串是不是回文。。。脑筋急转弯了- -

        def is_palindrome(s):
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        return 1 if is_palindrome(s) else 2
        
"""
https://leetcode-cn.com/submissions/detail/261192761/

执行用时：32 ms, 在所有 Python3 提交中击败了65.50%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了85.38%的用户
通过测试用例：
48 / 48
"""
