import functools
class Solution:
    def minDays(self, n: int) -> int:
        @functools.lru_cache(None)
        def dpi(i):
            if i == 1 or i == 2:
                return i
            elif i % 2 != 0 and i % 3 != 0:
                return 1 + dpi(i-1)
            elif i % 2 != 0 and i % 3 == 0:
                return min(1 + dpi(i-1), 1 + dpi(i//3))
            elif i % 2 == 0 and i % 3 != 0:
                return min(1 + dpi(i-1), 1 + dpi(i//2))
            else:
                return min(1 + dpi(i-1), 1 + dpi(i//2), 1 + dpi(i//3))
        return dpi(n)
    
"""
https://leetcode-cn.com/submissions/detail/98565385/

56 / 176 个通过测试用例
状态：执行出错

执行出错信息：
Line 11: RecursionError: maximum recursion depth exceeded
最后执行的输入：
69652
"""
