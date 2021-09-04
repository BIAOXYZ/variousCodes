class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 故意写一个会超时的记忆化搜索版本，超时原因就是：
        # 没有缓存之前已经计算好的 fib(i)，从而不能复用之前的计算结果。

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
"""
https://leetcode-cn.com/submissions/detail/215018710/

20 / 51 个通过测试用例
状态：超出时间限制

最后执行的输入：
37
"""
