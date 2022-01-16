# 官方 `方法二：矩阵快速幂` 直接用了个 numpy。。。我就是想试试是不是真的能用- -
import numpy as np
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        factor = np.mat([(0, 1, 0, 0, 0), (1, 0, 1, 0, 0), (1, 1, 0, 1, 1), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0)], np.dtype('O'))
        res = np.mat([(1, 1, 1, 1, 1)], np.dtype('O'))
        n -= 1
        while n > 0:
            if n % 2 == 1:
                res = res * factor % 1000000007
            factor = factor * factor % 1000000007
            n = n // 2
        return res.sum() % 1000000007
        
"""
https://leetcode-cn.com/submissions/detail/259233283/

执行用时：100 ms, 在所有 Python3 提交中击败了75.76%的用户
内存消耗：31.6 MB, 在所有 Python3 提交中击败了39.39%的用户
通过测试用例：
43 / 43
"""
"""
第一次知道 LeetCode 还能用 numpy 的。。。而且还是官方用的- -
"""
