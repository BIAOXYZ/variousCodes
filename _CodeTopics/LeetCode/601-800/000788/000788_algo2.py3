class Solution:
    def rotatedDigits(self, n: int) -> int:

        s = str(n)
        length = len(s)
        
        memoDic = {}
        def memorize_search(pos, canUseAnyDigit, has2569):
            if pos == length:
                return int(has2569)
            key = (pos, canUseAnyDigit, has2569)
            if key in memoDic:
                return memoDic[key]
            tmp = 0
            for digit in [0, 1, 2, 5, 6, 8, 9]:
                if not canUseAnyDigit and digit > int(s[pos]):
                    break
                tmp += memorize_search(
                    pos+1,
                    canUseAnyDigit or digit < int(s[pos]),
                    has2569 or (digit in [2, 5, 6, 9])
                    )
            memoDic[key] = tmp
            return memoDic[key]

        return memorize_search(0, False, False)
        
"""
https://leetcode.cn/submissions/detail/367193145/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
94.29%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
15.76%
的用户
通过测试用例：
50 / 50
"""
