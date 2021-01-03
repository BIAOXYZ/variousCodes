class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 直接用trivial的自顶向下递归应该会超时，但是还是先这么写一个。
        # 后来看了下 `LC70 爬楼梯` 里的提交 `TLE--000070.py`，里面注释里写的是：n到36或以上才会超时。
        # 但是首先这个题输入范围n最多到30；其次我试了下n=37时，结果（24157817）都算出来了。。。

        if n == 0: return 0
        elif n == 1: return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
"""
https://leetcode-cn.com/submissions/detail/135721611/

31 / 31 个通过测试用例
状态：通过
执行用时: 776 ms
内存消耗: 13 MB

执行用时：776 ms, 在所有 Python 提交中击败了19.23%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了25.00%的用户
"""
