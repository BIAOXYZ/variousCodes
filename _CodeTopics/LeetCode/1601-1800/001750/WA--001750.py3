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
        return right - left + 1 if left < right else 0
        
"""
https://leetcode.cn/submissions/detail/391421483/

94 / 100 个通过测试用例
状态：解答错误

输入：
"bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
输出：
0
预期结果：
1
"""
