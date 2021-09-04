class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 矩阵快速幂实现。
        # 该算法的核心是把斐波那契数列变换的过程抽象成 n 次（实际上 n - 1 次就够了）矩阵乘法。
        # 既然是矩阵幂运算，那么可以得到 log 级别的加速。

        if n < 2:
            return n
        MOD = 10**9 + 7

        def matrix_multiply(mat1, mat2):
            res = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        res[i][j] += mat1[i][k] * mat2[k][j]
                        res[i][j] %= MOD
            return res
        
        def matrix_pow(mat, n):
            res = [[1, 0], [0, 1]]
            curr = mat
            while n > 0:
                if n & 1 == 1:
                    res = matrix_multiply(res, curr)
                n >>= 1
                curr = matrix_multiply(curr, curr)
            return res
        
        mat = [[1,1], [1,0]]
        matPowRes = matrix_pow(mat, n-1)
        # 本来矩阵幂乘计算过后的结果还要和初始的斐波那契向量 [fib(1), fib(0)] 乘一下，去结果的第一个位置。
        # 但这里恰好是 [1, 0]，所以 matPowRes 的第 [0][0] 个位置的值就是答案了。
        return matPowRes[0][0]
        
"""
https://leetcode-cn.com/submissions/detail/215136784/

51 / 51 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB

执行用时：20 ms, 在所有 Python 提交中击败了36.64%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了59.47%的用户
"""
