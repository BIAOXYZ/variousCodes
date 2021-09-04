from functools import lru_cache
class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        # 记忆化搜索版本 -- 使用 functools 库里的缓存模块。
        # 由于只有 Python3 版本的 functools 才有缓存模块，只能切换到 py3 来写。
        # Python2 有 functools，但是没有缓存相关的装饰器。。。

        MOD = 10**9 + 7
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.fib(n-1) + self.fib(n-2)) % MOD
        
"""
https://leetcode-cn.com/submissions/detail/215033521/

51 / 51 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 15 MB

执行用时：40 ms, 在所有 Python3 提交中击败了29.72%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了16.13%的用户
"""
