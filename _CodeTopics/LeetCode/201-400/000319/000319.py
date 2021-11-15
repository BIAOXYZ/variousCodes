class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 以 6 为例，位置 6 上的灯泡会在 1、2、3、6 轮被操作——也就是说，在自己的因子所在的轮数被操作。
        # 那么对于任何位置来说，如果不是完全平方数（比如 6），会被操作偶数次；
        # 如果是完全平方数（比如 1、4、9），会被操作奇数次。

        if n == 0:
            return 0
        
        res = 0
        i = 1
        while i * i <= n:
            res += 1
            i += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/238948735/

执行用时：8 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了7.50%的用户
通过测试用例：
35 / 35
"""
