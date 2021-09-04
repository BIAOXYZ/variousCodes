class Solution(object):
    # 通过手动维护一个字典来解决 plain 的记忆化搜索超时问题。
    # 这次不用类变量，而是用类成员变量。
    # 和 https://leetcode-cn.com/submissions/detail/215026680/ 比起来差别确实不大，但实际上不一样。
    def __init__(self):
        self.memoCache = {0:0, 1:1}
    
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        MOD = 10**9 + 7
        if n in self.memoCache:
            return self.memoCache[n]
        else:
            val = self.fib(n-1) + self.fib(n-2)
            self.memoCache[n] = val % MOD
            return self.memoCache[n]
        
"""
https://leetcode-cn.com/submissions/detail/215028633/

51 / 51 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了36.64%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了12.84%的用户
"""
