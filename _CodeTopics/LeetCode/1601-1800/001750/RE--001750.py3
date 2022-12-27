class Solution:
    def minimumLength(self, s: str) -> int:

        n = len(s)
        left, right = 0, n-1
        while left < right and s[left] == s[right]:
            while s[left+1] == s[left]:
                left += 1
            while s[right-1] == s[right]:
                right -= 1
            left += 1
            right -= 1
        return right - left + 1 if left < right else 1 if left == right else 0
        
"""
https://leetcode.cn/submissions/detail/391421639/

98 / 100 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: string index out of range
    while s[left+1] == s[left]:
Line 7 in minimumLength (Solution.py)
    ret = Solution().minimumLength(param_1)
Line 35 in _driver (Solution.py)
    _driver()
Line 46 in <module> (Solution.py)
最后执行的输入：
"bbbbbbbbbbbbbbbbbbb"
"""
