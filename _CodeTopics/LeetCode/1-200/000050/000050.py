class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        N = -n if n < 0 else n
        string_N = str(bin(N))[2:]
        length = len(string_N)

        currMultiplier, res = x, 1
        for i in range(length-1,-1,-1):
            if string_N[i] == '1':
                res *= currMultiplier
            currMultiplier *= currMultiplier
        return 1/res if n < 0 else res
        
"""
https://leetcode-cn.com/submissions/detail/121113571/

304 / 304 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了89.75%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了5.01%的用户
"""
