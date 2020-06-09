class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        # 最朴素的递归会超时，原因是有很多重复计算：比如 self.climbStairs(n-2) 就要被分别计算两次。
        # 解决办法就是从原来的自顶向下，变为自底向上。
        """

        tmpres = [1,1,2]
        if n <= 2:
            return tmpres[n]
        else:
            smaller = tmpres[1]
            larger = tmpres[2]
            for i in range(3,n+1):
                res = larger + smaller
                smaller = larger
                larger = res
            return res
            
"""
# https://leetcode-cn.com/submissions/detail/77616284/

45 / 45 个通过测试用例
状态：通过
执行用时：16 ms
内存消耗：12.9 MB
"""
