class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        totalnum = 0
        arr = [2 * i + 1 for i in range(n)]
        for i in range(n/2):
            if arr[i] != arr[n-1-i]:
                diff = (arr[n-1-i] - arr[i]) / 2 
                totalnum += diff
        return totalnum
    
"""
https://leetcode-cn.com/submissions/detail/98529977/

301 / 301 个通过测试用例
状态：通过
执行用时：144 ms
内存消耗：13 MB
"""
