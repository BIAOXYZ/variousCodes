class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, n):
                if i*i > n:
                    break
                if n % i == 0:
                    return False
            return True

        MOD = 10**9+7
        n_prime = 0
        for i in range(1, n+1):
            if is_prime(i):
                n_prime += 1
        return math.prod(list(range(1, n_prime+1))) * math.prod(list(range(1, n - n_prime + 1))) % MOD
        
"""
https://leetcode.cn/submissions/detail/330980577/

执行用时：
28 ms
, 在所有 Python3 提交中击败了
97.59%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
35.34%
的用户
通过测试用例：
100 / 100
"""
