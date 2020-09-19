class Solution(object):
    def paintingPlan(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        # 艹，我猜就是这里错的！因为如果k值等于0反而有一种方法（什么也不涂），其他的小于n的就没有了。
        if 1 < k < n:
            return 0
        if k == n * n:
            return 1
        
        # quotient, remainder 
        # quo, rem = n / k, n % k
        
        def factorial(n):
          res = 1
          for i in range(1,n+1):
            res *= i
          return res

        def combinatorial_count(n, x):
            if x == 0 or x == n:
                return 1
            return factorial(n) / (factorial(x)*factorial(n-x))
                
        res = 0
        for i in range(n):
            for j in range(n):
                if n*(i+j) - i*j == k:
                    res += combinatorial_count(n, i) * combinatorial_count(n, j)
        return res
    
"""
https://leetcode-cn.com/contest/season/2020-fall/submissions/109519904/
"""
