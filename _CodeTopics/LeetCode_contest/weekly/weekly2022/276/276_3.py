class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        
        n = len(questions)
        # dp[i] 表示 questions 数组里以位置 i 开头的子数组的最高得分。
        dp = [-1] * n
        dp[-1] = questions[-1][0]
        
        for i in range(n-2, -1, -1):
            p, bp = questions[i][0], questions[i][1]
            if i + bp < n - 1:
                dp[i] = max(dp[i+1], p + dp[i+bp+1])
            else:
                dp[i] = max(dp[i+1], p)
        return dp[0]
    
"""
https://leetcode-cn.com/submissions/detail/258942513/

54 / 54 个通过测试用例
状态：通过
执行用时: 200 ms
内存消耗: 48.2 MB
"""
