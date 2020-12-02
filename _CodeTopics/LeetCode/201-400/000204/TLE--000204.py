import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        def is_prime(num):
            if num == 0 or num == 1:
                return False
            sqroot = int(round(math.sqrt(num))) + 1
            for i in range(2, sqroot):
                if num % i == 0:
                    return False
            return True

        res = 0
        for i in range(n):
            if is_prime(i):
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/128143922/

18 / 20 个通过测试用例
状态：超出时间限制

最后执行的输入：
999983
"""
