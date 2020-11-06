class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # 递归写法。
        def square_helper(num):
            if num == 0:
                return 1.0
            y = square_helper(num/2)
            return y*y if num % 2 == 0 else y*y*x

        N = -n if n < 0 else n
        res = square_helper(N)
        return 1/res if n < 0 else res
        
"""
https://leetcode-cn.com/submissions/detail/121464383/

304 / 304 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.2 MB

执行用时：12 ms, 在所有 Python 提交中击败了97.55%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.09%的用户
"""
