class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 1，2，3 先手胜；4 先手负。
        # 对于 5，6，7，也是先手胜：因为先手可以分别拿掉1，2，3个，剩下4个给后手，此时后手就必败了；
        ## 对于 8，变成先手负：先手不论拿几个，后手拿 4-x 个即可。
        # 综上，不能被 4 整除的话，先手胜；反之先手负。

        return n % 4 != 0
        
"""
https://leetcode-cn.com/submissions/detail/220570213/

60 / 60 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.4 MB

执行用时：16 ms, 在所有 Python 提交中击败了67.48%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了5.16%的用户
"""
