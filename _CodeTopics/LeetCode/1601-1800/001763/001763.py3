class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        # print(ord('A'),ord('Z'),ord('a'),ord('z'))
        # 65 90 97 122
        
        n = len(s)
        if n < 2:
            return ''

        def is_nice_string(s):
            se = set(s)
            for ch in s:
                if ch.lower() not in se or ch.upper() not in se:
                    return False
            return True

        curr = ''
        for i in range(n-1):
            for j in range(i+1, n):
                if is_nice_string(s[i:j+1]) and len(curr) < j + 1 - i:
                    curr = s[i:j+1]
        return curr
        
"""
https://leetcode-cn.com/submissions/detail/263999981/

执行用时：148 ms, 在所有 Python3 提交中击败了21.15%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了91.83%的用户
通过测试用例：
73 / 73
"""
