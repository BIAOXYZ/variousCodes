import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 上一个超时是因为每次都重复计算了is_prime()，同时每个is_prime()里循环太多了。
        # 改进一下，保持一个list来存储当前已知的素数，改进is_prime()里的那个循环，变成只除素数。

        primeList = [2]
        def is_prime(num):
            if num == 0 or num == 1:
                return False
            sqroot = int(math.sqrt(num))
            for prime in primeList:
                if prime > sqroot:
                    break
                if num % prime == 0:
                    return False
            primeList.append(num)
            return True

        res = 0
        for i in range(n):
            if is_prime(i):
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/128144898/

20 / 20 个通过测试用例
状态：通过
执行用时: 3904 ms
内存消耗: 59.9 MB

执行用时：3904 ms, 在所有 Python 提交中击败了5.02%的用户
内存消耗：59.9 MB, 在所有 Python 提交中击败了54.14%的用户
"""
