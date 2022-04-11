class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # official
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res
        
"""
https://leetcode-cn.com/submissions/detail/298600147/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
38.54%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
63.07%
的用户
通过测试用例：
9 / 9
"""
