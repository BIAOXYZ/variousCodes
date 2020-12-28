class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        totalnum = 0
        arr = [2 * i + 1 for i in range(n)]
        for i in range(n/2):
            while arr[i] != arr[n-1-i]:
                arr[i] += 1
                arr[n-1-i] -= 1
                totalnum += 1
        return totalnum
    
"""
https://leetcode-cn.com/submissions/detail/98528054/

104 / 301 个通过测试用例
状态：超出时间限制

最后执行的输入：
9809
"""
