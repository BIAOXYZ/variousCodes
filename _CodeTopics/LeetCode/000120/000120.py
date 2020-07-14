class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle:
            return 0
        
        length = len(triangle)
        dp = [[0] * i for i in range(1,length+1)]
        dp[0][0] = triangle[0][0]

        for i in range(1,length):
            templen = len(triangle[i])
            for j in range(templen):
                if j == 0: dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == templen - 1: dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j] 
        return min(dp[length-1])
        
"""
https://leetcode-cn.com/submissions/detail/87784293/

43 / 43 个通过测试用例
状态：通过
执行用时：20 ms
内存消耗：13.6 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了91.13%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了14.29%的用户
"""
